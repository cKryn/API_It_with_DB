"""
This module defines constants used throughout the project.

The constants are designed to provide reusable and centralized values,
ensuring consistency and maintainability across the application.

Constants:
- `WORK_DIR`: The root working directory of the project, determined dynamically
  based on the location of this file.
"""

from pathlib import Path

# Define the working directory as the project's root directory
WORK_DIR = Path(__file__).parent.parent
