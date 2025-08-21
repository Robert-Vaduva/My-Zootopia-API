"""
This module provides functionality to retrieve animal data from an external API.

It defines a function `fetch_data(animal_name)` which queries the API using the
given animal name and returns a list of matching animals in JSON format.
"""


import os
import requests
from dotenv import load_dotenv


# Load environment variables from .env
load_dotenv()
API_URL = 'https://api.api-ninjas.com/v1/animals?name='
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    """Fetch a list of animals from the API matching the given animal name."""
    list_of_animals = []
    response = requests.get(API_URL + animal_name, headers={'X-Api-Key': f'{API_KEY}'})
    animals = response.json()
    for animal in animals:
        list_of_animals.append(animal)
    return list_of_animals
