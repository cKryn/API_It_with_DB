"""
This script initializes a FastAPI application for managing IT trainers and courses.
It uses web scraping to collect data from external sources, processes it into structured
formats, and stores it in a database. The application exposes endpoints for querying
and modifying trainers and courses data.

Key Components:
- Database Initialization: Creates tables using SQLAlchemy.
- Data Ingestion: Scrapes trainer and course information from a specified website.
- FastAPI Endpoints: Provides RESTful APIs for managing trainers and courses.
"""
import pandas as pd
from fastapi import FastAPI, HTTPException, Depends
from src.db import SessionLocal, Base, engine, Session
from src.models import Trainers, Courses
from src.schemas import TrainerInput, CourseInput
from src.itschool_trainers_scrapper import SchoolScrapperInstructors
from src.itschool_courses_scrapper import SchoolScrapperCourses

# Initialize FastAPI application
app = FastAPI()

def init_db():
    """
    Initialize the database by creating all required tables.
    This function uses SQLAlchemy's metadata to generate tables in the database.
    """
    Base.metadata.create_all(bind=engine)

def get_db():
    """
    Provide a database session for the application.

    Yields:
        db (SessionLocal): A SQLAlchemy session instance.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Inserting data into SQL -> TRAINERS
trainers_scrapper = SchoolScrapperInstructors("https://itschool.ro/despre/traineri")
names = trainers_scrapper.name_data()
jobs = trainers_scrapper.job_data()
descriptions = trainers_scrapper.description_data()

# Creating a DataFrame for trainers and inserting into the database
df = pd.DataFrame({
    "name": names,
    "experience": jobs,
    "description": descriptions
})
df.to_sql("it_trainers", engine, if_exists="replace")

# Inserting data into SQL -> COURSES
courses_scrapper = SchoolScrapperCourses("https://itschool.ro/cursuri")
course_names = courses_scrapper.course_name()
start_data = courses_scrapper.start_date()
session_type = courses_scrapper.session_type()
certificated = courses_scrapper.certificated()

# Creating a DataFrame for courses and inserting into the database
df = pd.DataFrame({
    "course_names": course_names,
    "start_data": start_data,
    "description": session_type,
    "certificated": certificated
})
df.to_sql("it_courses", engine, if_exists="replace")

# FASTAPI EVENT
@app.on_event("startup")
def startup():
    """
    Event handler that runs at application startup.
    Initializes the database by creating all tables.
    """
    init_db()

@app.get("/trainers")
async def get_trainers(trainer: str | None = None, db: Session = Depends(get_db)):
    """
    Retrieve all trainers or filter by a specific trainer name.

    Args:
        trainer (str | None): Name of the trainer to filter (optional).
        db (Session): Database session (provided via dependency).

    Returns:
        List[Trainers]: List of all trainers or filtered trainers.
    """
    all_trainers = db.query(Trainers).all()

    if trainer:
        all_trainers = [t for t in all_trainers if trainer in t.name]

    return all_trainers

@app.post("/trainers")
async def add_trainer(trainer: TrainerInput, db: Session = Depends(get_db)):
    """
    Add a new trainer to the database.

    Args:
        trainer (TrainerInput): Trainer data to add.
        db (Session): Database session (provided via dependency).

    Raises:
        HTTPException: If a trainer with the same ID already exists.

    Returns:
        dict: Confirmation message and details of the added trainer.
    """
    if db.query(Trainers).filter(Trainers.id == trainer.id).first():
        raise HTTPException(status_code=400, detail="Trainer with the ID already exists.")

    new_trainer = Trainers(**trainer.model_dump())
    db.add(new_trainer)
    db.commit()
    db.refresh(new_trainer)
    return {"message": "Trainer added successfully", "Trainer": new_trainer}

@app.get("/courses")
async def get_course(course: str | None = None, db: Session = Depends(get_db)):
    """
    Retrieve all courses or filter by a specific course name.

    Args:
        course (str | None): Name of the course to filter (optional).
        db (Session): Database session (provided via dependency).

    Returns:
        List[Courses]: List of all courses or filtered courses.
    """
    all_courses = db.query(Courses).all()

    if course:
        all_courses = [c for c in all_courses if course in c.name]

    return all_courses

@app.post("/courses")
async def add_course(course: CourseInput, db: Session = Depends(get_db)):
    """
    Add a new course to the database.

    Args:
        course (CourseInput): Course data to add.
        db (Session): Database session (provided via dependency).

    Raises:
        HTTPException: If a course with the same ID already exists.

    Returns:
        dict: Confirmation message and details of the added course.
    """
    if db.query(Courses).filter(Courses.id == course.id).first():
        raise HTTPException(status_code=400, detail="Course with the ID already exists.")

    new_course = Courses(**course.model_dump())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return {"message": "Course added successfully", "Course": new_course}
