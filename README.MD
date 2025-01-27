# API IT with DB

This project demonstrates how to build a FastAPI-based application for managing IT trainers and courses. The application integrates web scraping, a relational database, and a REST API to provide a full-stack solution.

## Project Structure

```
API_It_with_DB
|-- .env                   # Environment variables file (excluded from version control)
|-- .env_example           # Example environment file for configuration
|-- .gitignore             # Ignored files for Git
|-- main.py                # Main entry point for the FastAPI application
|-- requirements.txt       # Python dependencies
|-- src/                   # Source code folder
    |-- __init__.py        # Marks the directory as a Python package
    |-- constants.py       # Contains global constants like project root directory
    |-- db.py              # Database configuration and SQLAlchemy setup
    |-- display_example.py # Streamlit app for searching trainers
    |-- itschool_courses_scrapper.py  # Scraper for course data
    |-- itschool_trainers_scrapper.py # Scraper for trainer data
    |-- models.py          # ORM models for database tables
    |-- schemas.py         # Pydantic models for request validation
```

## Features

- **Web Scraping**:
  - `itschool_courses_scrapper.py`: Extracts course details (names, start dates, etc.)
  - `itschool_trainers_scrapper.py`: Extracts trainer details (names, jobs, etc.)

- **Database Integration**:
  - Uses SQLAlchemy for database modeling and interaction.
  - `.env` file for storing sensitive credentials (e.g., MySQL username and password).

- **FastAPI REST Endpoints**:
  - CRUD operations for trainers and courses.
  - Routes:
    - `/trainers` (GET, POST)
    - `/courses` (GET, POST)

- **Frontend**:
  - A Streamlit-based interface (`display_example.py`) for searching trainers by name.

## Setup Instructions

### Prerequisites

- Python 3.9+
- MySQL database

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/cKryn/API_It_with_DB.git
    cd API_It_with_DB
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure `.env` file:
    - Copy `.env_example` to `.env`.
    - Update `MYSQL_USERNAME` and `MYSQL_PASSWORD` with your database credentials.

4. Initialize the database:
    - Ensure your MySQL server is running.
    - Run the FastAPI application to create tables.

5. Start the application:
    ```bash
    uvicorn main:app --reload --host 127.0.0.1 --port 9001
    ```

6. Run the Streamlit app (optional):
    ```bash
    streamlit run src/display_example.py
    ```

## API Endpoints

- `GET /trainers`: Retrieve all trainers.
- `POST /trainers`: Add a new trainer.
- `GET /courses`: Retrieve all courses.
- `POST /courses`: Add a new course.

## Technologies Used

- **Backend**: FastAPI, SQLAlchemy
- **Frontend**: Streamlit
- **Database**: MySQL
- **Web Scraping**: BeautifulSoup, Requests

## Folder Highlights

- `src/constants.py`: Centralized constants, including project root.
- `src/db.py`: Handles database connection and session management.
- `src/models.py`: Defines the database tables (ORM).
- `src/schemas.py`: Pydantic models for request validation.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.
