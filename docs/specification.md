# SoloMind — Business Launch Tracker — Specification

## Purpose

SoloMind helps beginners organise the steps required to start an online business selling physical or digital products. The application allows users to manage business launch tasks and track their progress.

## Entities

### Task
- id (integer, primary key)
- title (text, required, max 200 characters)
- description (text, optional)
- status (one of: todo, in_progress, done — default todo)
- created_at (timestamp)
- due_date (date, optional)

## Routes

| Method | Path | Does |
|---|---|---|
| GET | / | List all tasks, newest first |
| GET | /task/new | Show the form to create a task |
| POST | /task | Create a task and redirect to / |
| GET | /task/<id> | Show the details of one task |
| POST | /task/<id>/status | Update the task status and redirect back |

## Technical Constraints

- Python 3.11+ and Flask 3.x
- SQLite using the Python standard library sqlite3
- Jinja2 templates in the templates/ folder, with one base template
- No authentication
- No JavaScript framework
- Use the existing lowcode-project repository
- Preserve the existing Week 2 contact form functionality

## Out of Scope

- AI business recommendations or chatbot
- Automatic product and supplier research
- Sales funnel automation
- Payment processing
- User accounts and authentication
- Automated reminders
- File attachments
- External APIs

## Future Vision

SoloMind may later evolve into an AI-assisted business copilot that helps beginners discover product opportunities, validate business ideas, develop marketing strategies and plan an online business launch.