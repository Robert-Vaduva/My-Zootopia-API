import requests


API_URL = 'https://api.api-ninjas.com/v1/animals?name='
API_KEY = "IvLPDV+GnuYbo+XJr2VjeA==Saj417C9U3BISPBz"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
        },
    'locations': [
      ...
        ],
    'characteristics': {
      ...
        }
    },
    """
    list_of_animals = []
    response = requests.get(API_URL + animal_name, headers={'X-Api-Key': f'{API_KEY}'})
    animals = response.json()
    for animal in animals:
        list_of_animals.append(animal)
    return list_of_animals


if __name__ == "__main__":
    print(fetch_data(str(input("Enter a name of an animal: "))))
