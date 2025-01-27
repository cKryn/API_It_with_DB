"""
This module defines the Pydantic models used for data validation and serialization in the application.

Models:
- `TrainerInput`: Schema for trainer input data, ensuring type validation and optional fields.
- `CourseInput`: Schema for course input data, with fields for course details and certification status.

These models provide structure and type safety for incoming data in API requests.
"""

from pydantic import BaseModel
from typing import Optional

class TrainerInput(BaseModel):
    """
    Pydantic model for validating trainer input data.

    Attributes:
        index (int): Unique identifier for the trainer.
        name (str): Name of the trainer.
        experience (str): Professional experience of the trainer.
        description (Optional[str]): Additional description or biography of the trainer (optional).
    """
    index: int
    name: str
    experience: str
    description: Optional[str] | None = None

class CourseInput(BaseModel):
    """
    Pydantic model for validating course input data.

    Attributes:
        index (int): Unique identifier for the course.
        course_names (str): Name of the course.
        start_data (str): Start date of the course.
        description (str): Description or session type of the course.
        certificated (Optional[bool]): Indicates whether the course provides certification (optional).
    """
    index: int
    course_names: str
    start_data: str
    description: str
    certificated: Optional[bool] | None = None