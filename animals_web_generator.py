import json


def serialize_animal(animal_obj):
    """
    Convert a single animal object into an HTML <li> card string.
    """
    output = ""

    output += '<li class="cards__item">\n'

    # Title (Name)
    if "name" in animal_obj:
        output += '  <div class="card__title">' + animal_obj["name"] + "</div>\n"

    output += '  <p class="card__text">\n'

    # Subtitle (Scientific Name)
    if "taxonomy" in animal_obj and "scientific_name" in animal_obj["taxonomy"]:
        sci = animal_obj["taxonomy"]["scientific_name"]
        output += '  <div class="card__subtitle"><em>' + sci + "</em></div>\n"

    # Diet
    if "characteristics" in animal_obj and "diet" in animal_obj["characteristics"]:
        diet = animal_obj["characteristics"]["diet"]
        output += "      <strong>Diet:</strong> " + diet + "<br/>\n"

    # First location
    if "locations" in animal_obj and len(animal_obj["locations"]) > 0:
        location = animal_obj["locations"][0]
        output += "      <strong>Location:</strong> " + location + "<br/>\n"

    # Type
    if "characteristics" in animal_obj and "type" in animal_obj["characteristics"]:
        animal_type = animal_obj["characteristics"]["type"]
        output += "      <strong>Type:</strong> " + animal_type + "<br/>\n"

    output += "  </p>\n"
    output += "</li>\n\n"

    return output


def build_animals_output(animals):
    """
    Build the full HTML string for all animals.
    """
    output = ""
    for animal_obj in animals:
        output += serialize_animal(animal_obj)
    return output


def read_file(filepath):
    """
    Read and return the content of a text file.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def write_file(filepath, content):
    """
    Write the given content to a text file.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    """
    Main program function.
    Reads data, builds HTML, and writes output file.
    """
    animals = json.loads(read_file("animals_data.json"))
    html_template = read_file("animals_template.html")

    animals_output = build_animals_output(animals)
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    write_file("animals.html", new_html)
    print("animals.html has been created.")


main()
