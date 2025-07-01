# Task Manager Project

## Overview

This project is a simple task manager.
It focuses on:

- Practicing **Python OOP clean design**
- Building a **FastAPI interface**
- Developing a minimal **React frontend**
- Integrating with a **database for persistence**

The system allows adding, editing, deleting, toggling, and listing tasks, each with:

- `taskId`
- `description`
- `difficulty` (easy, medium, hard)
- `is_completed` status

---

## Current Project Structure

├── manager.py # TaskManager: handles task operations
├── task.py # Task: represents a single task entity
├── utils.py # Shared types (e.g., TaskInput dataclass)
├── main.py # Entry point for testing / CLI
└── README.md

---

## Current Features

✅ Create tasks
✅ Edit task description / difficulty
✅ Toggle task completion
✅ Delete tasks
✅ List tasks

---

## Next Steps TODO

- [ ] Add **FastAPI endpoints** to expose task operations as REST API.
- [ ] Build a **React frontend** to interact with the API.
- [ ] Integrate a **database backend** (PostgresSQL) to persist tasks

## Focus/Goals

- Strengthen Python OOP design skills.
- Re-Learn how to connect backend flawlessly (Python + FastAPI) to frontend (React)
- Practice full-stack development with clean architecture principles.
