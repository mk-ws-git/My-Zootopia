import json

def main():
    # Read animals data
    with open("animals_data.json", "r", encoding="utf-8") as f:
        animals = json.load(f)

    animals_output = ""

    for animal in animals:
        animals_output += '<li class="cards__item">\n'

        # Title (Name)
        if "name" in animal:
            animals_output += '  <div class="card__title">' + animal["name"] + '</div>\n'

        animals_output += '  <p class="card__text">\n'

        # Diet
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            animals_output += '      <strong>Diet:</strong> ' + animal["characteristics"]["diet"] + '<br/>\n'

        # First location
        if "locations" in animal and len(animal["locations"]) > 0:
            animals_output += '      <strong>Location:</strong> ' + animal["locations"][0] + '<br/>\n'

        # Type
        if "characteristics" in animal and "type" in animal["characteristics"]:
            animals_output += '      <strong>Type:</strong> ' + animal["characteristics"]["type"] + '<br/>\n'

        animals_output += '  </p>\n'
        animals_output += '</li>\n\n'

    # Read HTML template
    with open("animals_template.html", "r", encoding="utf-8") as f:
        html_template = f.read()

    # Replace placeholder with animals output
    new_html = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    # Write new HTML file
    with open("animals.html", "w", encoding="utf-8") as f:
        f.write(new_html)

    print("animals.html has been created.")

# Run the program
main()
