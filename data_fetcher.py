"""
This module provides utilities for retrieving animal data from an external API.

It supports two main methods:
- `fetch_data_from_file(file_path)`: Load animal data from a local JSON file.
- `fetch_data_from_api(animal_name)`: Query the external API (API Ninjas) for
  animals matching the given name, using an API key stored in environment variables.

Environment variables are loaded from a `.env` file using `python-dotenv`.
Required variable:
- API_KEY: the authentication key for accessing the API.
"""


import os
import requests
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()
API_URL = 'https://api.api-ninjas.com/v1/animals?name='
API_KEY = os.getenv('API_KEY')


def fetch_data_from_file(file_path):
    """Load JSON data from a given file path."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()
        return data
    except FileNotFoundError as error:
        print("There has been an error ...", error)
        return None


def fetch_data_from_api(animal_name):
    """Fetch a list of animals from the API matching the given animal name."""
    list_of_animals = []
    response = requests.get(API_URL + animal_name, headers={'X-Api-Key': f'{API_KEY}'})
    animals = response.json()
    for animal in animals:
        list_of_animals.append(animal)
    return list_of_animals
