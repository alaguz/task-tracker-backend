from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from datetime import datetime

app = Flask(__name__)
CORS(app)

def get_db():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()
    return jsonify([dict(task) for task in tasks])

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    conn = get_db()
    conn.execute('INSERT INTO tasks (text, done, created_at) VALUES (?, ?, ?)',
                (data['text'], False, datetime.now().isoformat()))
    conn.commit()
    conn.close()
    return jsonify({'success': True}), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.json
    conn = get_db()
    if 'done' in data:
        conn.execute('UPDATE tasks SET done = ? WHERE id = ?', (data['done'], id))
    if 'text' in data:
        conn.execute('UPDATE tasks SET text = ? WHERE id = ?', (data['text'], id))
    conn.commit()
    conn.close()
    return jsonify({'success': True})


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db()
    conn.execute('DELETE FROM tasks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

# Create table
with get_db() as conn:
    conn.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT NOT NULL,
        done BOOLEAN DEFAULT FALSE,
        created_at TEXT
    )''')
    conn.commit()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
