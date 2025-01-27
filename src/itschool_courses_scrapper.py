"""
This module defines the `SchoolScrapperCourses` class, which is used to scrape course information
from a specified webpage using the BeautifulSoup library.

The class provides methods to extract the following details about courses:
- Course names
- Start dates
- Session types
- Certification availability

Key Features:
- Handles HTTP requests to fetch webpage content.
- Parses HTML content to extract relevant data.
- Returns structured data for further processing.

Dependencies:
- requests: For making HTTP requests.
- BeautifulSoup (bs4): For parsing and scraping HTML content.
"""

import requests
from bs4 import BeautifulSoup

class SchoolScrapperCourses:
    """
    A web scraper for extracting course-related information from a given URL.

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

    def course_name(self):
        """
        Extract the names of the courses from the webpage.

        Returns:
            list: A list of course names as strings.
        """
        raw_data = self.soup.find_all("h3", {"class":"Typography__H3-"
                                                     "sc-wm63nk-2 ePxzQe"})
        course_names = []
        for tag in raw_data:
            course_names.append(tag.text.strip())
        return course_names

    def start_date(self):
        """
        Extract the start dates of the courses from the webpage.

        Returns:
            list: A list of start dates as strings.
        """
        raw_data = self.soup.find_all("p", {"class":"CourseCardstyle__"
                                                    "Date-sc-1szi4ub-9 eNCAjZ"})
        start_date_data = []
        for tag in raw_data:
            start_date_data.append(tag.text.strip())
        return start_date_data

    def session_type(self):
        """
        Extract the session types of the courses (e.g., online or in-person).

        Returns:
            list: A list of session types as strings.
        """
        raw_data = self.soup.find_all("p", {"class":"CourseCardstyle__"
                                                    "Location-sc-1szi4ub-8 dFYwnP"})
        session_type_data = []
        for tag in raw_data:
            session_type_data.append(tag.text.strip())
        return session_type_data

    def certificated(self):
        """
        Determine whether each course offers a certification recognized by the Ministry of Education.

        Returns:
            list: A list of boolean values indicating certification availability.
        """
        raw_data = self.soup.find_all("p", {"class":"Typography__"
                                                    "Description-sc-wm63nk-8 euMswu"})

        certificated_data = [tag.text.strip() for tag in raw_data]

        boolean_data = []

        for data in certificated_data:

            if data == "Certificare Ministerul Educației Naționale":
                boolean_data.append(True)
            else:
                boolean_data.append(False)
        return boolean_data
