"""
This module defines the `SchoolScrapperInstructors` class, which is used to scrape instructor information
from a specified webpage using the BeautifulSoup library.

The class provides methods to extract the following details about instructors:
- Names of the instructors
- Job titles or roles of the instructors
- Descriptions related to the instructors

Key Features:
- Handles HTTP requests to fetch webpage content.
- Parses HTML content to extract relevant instructor data.
- Returns structured data for further processing.

Dependencies:
- requests: For making HTTP requests.
- BeautifulSoup (bs4): For parsing and scraping HTML content.
"""

import requests
from bs4 import BeautifulSoup

class SchoolScrapperInstructors:
    """
    A web scraper for extracting instructor-related information from a given URL.

    Attributes:
        url (str): The URL of the webpage to scrape.
        response (Response): The HTTP response object for the requested URL.
        soup (BeautifulSoup): Parsed HTML content of the webpage.
    """

    def __init__(self, url):
        """
        Initialize the scraper with the target URL and fetch the webpage content.

        Args:
            url (str): The URL of the webpage to scrape.

        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
        """
        self.url = url
        self.response = requests.get(self.url, timeout=10)
        self.soup = BeautifulSoup(self.response.content, "lxml")

    def name_data(self):
        """
        Extract the names of the instructors from the webpage.

        Returns:
            list: A list of instructor names as strings.
        """
        raw_data = self.soup.find_all("h5", {"class":"Typography__H5-sc-wm63nk-4 ikRFWz"})
        instructor_names = []
        for tag in raw_data:
            instructor_names.append(tag.text.strip())
        return instructor_names

    def job_data(self):
        """
        Extract the job titles or roles of the instructors from the webpage.

        Returns:
            list: A list of job titles as strings.
        """
        raw_data = self.soup.find_all("p", {"class":"Typography__Body-sc-wm63nk"
                                                    "-7 LandingProgramsstyle__Description-sc-"
                                                    "1o6bj5c-3 koKZlH cvjzaS"})
        job_names = []
        for job in raw_data:
            job_names.append(job.text.strip())
        return job_names

    def description_data(self):
        """
        Extract descriptions related to the instructors from the webpage.

        Returns:
            list: A list of instructor descriptions as strings.
        """
        raw_data = self.soup.find_all("p", {"class": "Typography__Body-sc-wm63nk-7 "
                                                     "LandingProgramsstyle__Description-sc-"
                                                     "1o6bj5c-3 dXSXuu cvjzaS"})
        description_data = []
        for desc in raw_data:
            description_data.append(desc.text.strip())
        return description_data
