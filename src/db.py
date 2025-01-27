"""
This module handles the database setup and configuration for the application.

It uses SQLAlchemy to establish a connection to the database and provides the following:
- Engine: A core interface to the database.
- SessionLocal: A factory for creating database sessions.
- Base: A declarative base for defining ORM models.

Environment Variables:
- `MYSQL_USERNAME`: The username for the MySQL database.
- `MYSQL_PASSWORD`: The password for the MySQL database.

Constants:
- `mysql_url`: The connection URL for the MySQL database, dynamically built using environment variables.
- `engine`: The SQLAlchemy engine for database communication.
- `SessionLocal`: A sessionmaker instance configured with the database engine.
- `Base`: A declarative base class for defining database models.
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from src.constants import WORK_DIR

# Load environment variables from the .env file located in the project root
load_dotenv(WORK_DIR / ".env")

# Retrieve database credentials from environment variables
USERNAME = os.getenv("MYSQL_USERNAME")
PASSWORD = os.getenv("MYSQL_PASSWORD")

# Construct the MySQL connection URL
mysql_url = f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@localhost:3306/it_with_api'

# Create the SQLAlchemy engine for database communication
engine = create_engine(mysql_url)

# Create a session factory for interacting with the database
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Define the declarative base for ORM models
Base = declarative_base()
