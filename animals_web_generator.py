import json

def main():
    # Read animals data
    with open("animals_data.json", "r", encoding="utf-8") as f:
        animals = json.load(f)

    animals_output = ""   # holds ALL animals

    for animal in animals:
        animals_output += '<li class="cards__item">\n'

        # Name
        if "name" in animal:
            animals_output += "Name: " + animal["name"] + "<br/>\n"

        # Diet
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            animals_output += "Diet: " + animal["characteristics"]["diet"] + "<br/>\n"

        # First location
        if "locations" in animal and len(animal["locations"]) > 0:
            animals_output += "Location: " + animal["locations"][0] + "<br/>\n"

        # Type
        if "characteristics" in animal and "type" in animal["characteristics"]:
            animals_output += "Type: " + animal["characteristics"]["type"] + "<br/>\n"

        animals_output += "</li>\n"

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
