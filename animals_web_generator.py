"""Script to load animals data from JSON and print selected fields."""


import data_fetcher


TEMPLATE_PATH = "animals_template.html"
TARGET_PATH = "animals.html"
KEY_WORDS = "__REPLACE_ANIMALS_INFO__"


def get_and_format_animal_data(in_data):
    """Read animals data and print selected details for each animal."""
    output = "\n"
    for animal in in_data:
        output += '\t\t\t<li class="cards__item">'
        if "name" in animal:
            output += f"\n\t\t\t\t<div class='card__title'>{animal['name']}</div>\n"
        output += "\t\t\t\t<p class='card__text'>"
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output += (f"\n\t\t\t\t\t<strong>Diet:</strong> "
                       f"{animal['characteristics']['diet']}<br/>\n")
        if "locations" in animal:
            output += f"\t\t\t\t\t<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
        if "characteristics" in animal and "type" in animal["characteristics"]:
            output += (f"\t\t\t\t\t<strong>Type:</strong> "
                       f"{animal['characteristics']['type']}<br/>\n")
        output += "\t\t\t\t</p>"
        output += '\n\t\t\t</li>\n'
    return output


def get_html_template():
    """Load and return the HTML template from TEMPLATE_PATH."""
    return data_fetcher.fetch_data_from_file(TEMPLATE_PATH)


def generate_html(data):
    """Write the given HTML data to animals.html."""
    with open(TARGET_PATH, "w", encoding="utf-8") as file:
        file.write(data)
        print(f"Website was successfully generated to the file {TARGET_PATH}.")


def main():
    """Generate an HTML page with animal data using a template and API information."""
    animal_name = str(input("Enter a name of an animal: "))
    response = data_fetcher.fetch_data_from_api(animal_name)

    if response == ["error"]:
        animal_data = ("<h2>The API requires a key in order to work.</h2>"
                       "<h2>Please check the README for instructions.</h2>")
    else:
        if response:
            animal_data = get_and_format_animal_data(response)
        else:
            animal_data = f"<h2>The animal \"{animal_name}\" doesn't exist.</h2>"
    template = get_html_template()
    page = template.replace(KEY_WORDS, animal_data)
    generate_html(page)


if __name__ == "__main__":
    main()
