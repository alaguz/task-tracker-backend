# Task Tracker API

[![Live Demo](https://img.shields.io/badge/Live-Frontend-blue?logo=netlify)](https://gregarious-shortbread-678dc1.netlify.app/)
[![API](https://img.shields.io/badge/API-Active-green?logo=render)](https://task-tracker-api-y2qn.onrender.com/tasks)

Full-stack task management backend API powering the [live app](https://gregarious-shortbread-678dc1.netlify.app/).

## Overview
RESTful API for CRUD task operations with SQLite persistence. Supports add/read/update/delete tasks, toggle complete status.

## Tech Stack
- **Backend**: Python 3, Flask (routes: GET/POST/PUT/DELETE `/tasks/:id`)
- **Database**: SQLite (`tasks.db`: id, text, done, created_at)
- **CORS**: Flask-CORS (frontend access)
- **Deployment**: Render.com (auto-deploys from GitHub)
- **Frontend**: React/JS on Netlify (connects via this API)

## API Endpoints


GET /tasks # List all tasks (JSON array)
POST /tasks # Add { "text": "New task" }
PUT /tasks/:id # Update { "done": true } or { "text": "Updated" }
DELETE /tasks/:id # Delete task


**Live API**: https://task-tracker-api-y2qn.onrender.com/tasks [Test in browser]

## Local Setup
1. `pip install -r requirements.txt`
2. `python app.py`
3. http://127.0.0.1:5000/tasks

## Deployment
- GitHub: https://github.com/alaguz/task-tracker-backend
- Render: Auto-build `pip install -r requirements.txt`, start `python app.py` (host='0.0.0.0')

## Features Demonstrated
- Full CRUD, data persistence
- Production deployment (Render fixes: port binding, debug=False)
- CORS for React frontend
- Schema auto-init

Built for portfolio: end-to-end full-stack (React + Flask + SQLite).


## Update Repo
Power Shell , run
cd C:\Users\alanj\task-tracker\backend
notepad README.md
git add README.md
git commit -m "Polish README with badges/code blocks"
git push origin main

## Links:
https://gregarious-shortbread-678dc1.netlify.app/

https://task-tracker-api-y2qn.onrender.com/tasks

http://127.0.0.1:5000/tasks



## Extra:
powershell run
cd C:\Users\alanj\task-tracker\backend
dir  # Confirms app.py, tasks.db, requirements.txt

