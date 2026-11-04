# Low-Code Project

CCT College Dublin  
Certificate in Low-Code, No-Code & AI-Assisted Application Development

## About This Project

This repository contains my coursework for the CCT Low-Code, No-Code & AI-Assisted Application Development course.

The project started as a simple Flask application in Week 1 and has gradually developed into SoloMind — Business Launch Tracker.

## SoloMind — Business Launch Tracker

SoloMind helps beginners organise the steps required to start an online business selling physical or digital products.

The current application allows users to:

- Create business launch tasks.
- View tasks and their details.
- Set an optional due date.
- Update task status: To Do, In Progress or Done.
- Store tasks in a SQLite database.

The application also preserves the contact form developed in Week 2, including server-side validation.

## Technologies Used

- Python 3.13.16
- Flask 3.1.2
- SQLite
- Jinja2
- Visual Studio Code
- Git and GitHub

## How to Run the Application

1. Clone or download the repository.
2. Open the project folder in Terminal.
3. Create a virtual environment:

   `python3 -m venv .venv`

4. Activate the virtual environment:

   `source .venv/bin/activate`

5. Install the dependencies:

   `python -m pip install -r requirements.txt`

6. Start the application:

   `python app.py`

7. Open `http://127.0.0.1:5000` in your browser.

The SQLite database is created automatically in the `instance` folder when the application starts.

## Course Progress

### Week 1 — First Flask Application

- Created the initial Flask application with ChatGPT.
- Displayed "Hello from Leandro" in the browser.
- Configured Git and GitHub.
- Documented the original SoloMind concept.

### Week 2 — AI Tool Comparison

- Used Claude and Gemini to generate Flask contact forms.
- Compared and tested both implementations.
- Selected Claude's solution.
- Integrated the contact form into the main application.

### Week 3 — Building a Full Application

- Wrote `docs/specification.md` before generating code.
- Created the `feature/task-app` Git branch.
- Used Claude to generate the SoloMind task management application.
- Tested task creation, task details and status updates.
- Confirmed the Week 2 contact form still works.
- Used Gemini for an AI code review.
- Documented the review in `docs/week03-review.md`.

## Future Vision

The long-term goal is to develop SoloMind into an AI-assisted business copilot.

Possible future features include:

- Discovering online business opportunities.
- Researching physical and digital products.
- Helping users validate business ideas.
- Planning marketing strategies and sales funnels.
- Guiding users through the steps of launching an online business.

These AI features are not implemented in the current application.

## AI Tools Used

- **ChatGPT:** Initial Flask application and development guidance.
- **Claude:** Contact form implementation and Week 3 SoloMind application generation.
- **Gemini:** Week 2 comparison and Week 3 code review.

## Development Notes

This application is currently a coursework project, not a production-ready service.

The `.venv` directory and SQLite database files are excluded from Git using `.gitignore`.