"""Script to load animals data from JSON and print selected fields."""


import data_fetcher


TEMPLATE_PATH = "animals_template.html"
TARGET_PATH = "animals.html"
KEY_WORDS = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """Load JSON data from a given file path."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()
        return data
    except FileNotFoundError as error:
        print("There has been an error ...", error)
        return None


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
    return load_data(TEMPLATE_PATH)


def generate_html(data):
    """Write the given HTML data to animals.html."""
    with open(TARGET_PATH, "w", encoding="utf-8") as file:
        file.write(data)
        print(f"Website was successfully generated to the file {TARGET_PATH}.")


def main():
    """Generate an HTML page with animal data using a template."""
    name = str(input("Enter a name of an animal: "))
    response = data_fetcher.fetch_data(name)

    if response:
        animal_data = get_and_format_animal_data(response)
    else:
        animal_data = f"<h2>The animal \"{name}\" doesn't exist.</h2>"
    template = get_html_template()
    page = template.replace(KEY_WORDS, animal_data)
    generate_html(page)


if __name__ == "__main__":
    main()
