import json

def main():
    with open("animals_data.json", "r", encoding="utf-8") as f:
        animals = json.load(f)

    for animal in animals:

        # Name
        if "name" in animal:
            print("Name:", animal["name"])

        # Diet
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            print("Diet:", animal["characteristics"]["diet"])

        # First location
        if "locations" in animal and len(animal["locations"]) > 0:
            print("Location:", animal["locations"][0])

        # Type
        if "characteristics" in animal and "type" in animal["characteristics"]:
            print("Type:", animal["characteristics"]["type"])

        print()


# Run the program
main()