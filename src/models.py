"""
This module defines the ORM (Object-Relational Mapping) models for the application's database.

Models:
- `Trainers`: Represents the trainers with their details such as name, experience, and description.
- `Courses`: Represents the courses with details such as course names, start dates, session types, and certification status.

Each model is mapped to a corresponding table in the database.
"""

from sqlalchemy import Column, Integer, String
from src.db import Base

class Trainers(Base):
    """
    Represents the `it_trainers` table in the database.

    Attributes:
        index (int): Primary key, auto-incremented.
        name (str): Name of the trainer.
        experience (str): Professional experience of the trainer.
        description (str): Description or biography of the trainer.
    """
    __tablename__ = "it_trainers"

    index = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    experience = Column(String(60), nullable=False)
    description = Column(String(500), nullable=False)

    def __repr__(self):
        """
        Return a string representation of the `Trainer` instance.

        Returns:
            str: A formatted string representation of the trainer.
        """
        return f"Trainer(name={self.name})"

class Courses(Base):
    """
    Represents the `it_courses` table in the database.

    Attributes:
        index (int): Primary key, auto-incremented.
        course_names (str): Name of the course.
        start_data (str): Start date of the course.
        description (str): Description or session type of the course.
        certificated (str): Certification status of the course.
    """
    __tablename__ = "it_courses"

    index = Column(Integer, primary_key=True, autoincrement=True)
    course_names = Column(String(30), nullable=False)
    start_data = Column(String(60), nullable=False)
    description = Column(String(20), nullable=False)
    certificated = Column(String(10), nullable=False)