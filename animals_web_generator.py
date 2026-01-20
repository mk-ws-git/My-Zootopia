import json


def get_nested_value(obj, keys):
    """Return nested dict value or None."""
    current = obj
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def serialize_field(label, value):
    """Return one <li> field line or '' if missing."""
    if value is None:
        return ""
    if isinstance(value, str) and value.strip() == "":
        return ""
    return (
        '      <li class="card__list-item">'
        "<strong>" + label + ":</strong> "
        + str(value)
        + "</li>\n"
    )


def serialize_animal(animal_obj):
    """Return one animal card as HTML."""
    output = ""

    name = animal_obj.get("name")
    scientific_name = get_nested_value(animal_obj, ["taxonomy", "scientific_name"])
    characteristics = animal_obj.get("characteristics", {})
    locations = animal_obj.get("locations", [])

    output += '<li class="cards__item">\n'

    if name:
        output += '  <div class="card__title">' + name + "</div>\n"

    if scientific_name:
        output += '  <div class="card__subtitle"><em>' + scientific_name + "</em></div>\n"

    output += '  <div class="card__text">\n'
    output += '    <ul class="card__list">\n'

    output += serialize_field("Diet", characteristics.get("diet"))

    if isinstance(locations, list) and len(locations) > 0:
        output += serialize_field("Locations", ", ".join(locations))

    output += serialize_field("Type", characteristics.get("type"))
    output += serialize_field("Group", characteristics.get("group"))
    output += serialize_field("Habitat", characteristics.get("habitat"))
    output += serialize_field("Lifespan", characteristics.get("lifespan"))
    output += serialize_field("Top speed", characteristics.get("top_speed"))
    output += serialize_field("Weight", characteristics.get("weight"))
    output += serialize_field("Length", characteristics.get("length"))
    output += serialize_field("Distinctive feature", characteristics.get("distinctive_feature"))
    output += serialize_field("Temperament", characteristics.get("temperament"))
    output += serialize_field("Slogan", characteristics.get("slogan"))

    output += "    </ul>\n"
    output += "  </div>\n"
    output += "</li>\n"

    return output


def build_animals_output(animals):
    """Return HTML for all animal cards."""
    output = ""
    sorted_animals = sorted(animals, key=lambda a: a.get("name", "").lower())

    for animal_obj in sorted_animals:
        output += serialize_animal(animal_obj)
        output += "\n"

    return output


def read_file(filepath):
    """Read text file content."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def write_file(filepath, content):
    """Write text file content."""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    """Generate animals.html from JSON + template."""
    animals = json.loads(read_file("animals_data.json"))
    html_template = read_file("animals_template.html")

    animals_output = build_animals_output(animals)
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    write_file("animals.html", new_html)
    print("animals.html has been created.")


main()
