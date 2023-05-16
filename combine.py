import os
import json

def combine_and_convert_json_files(input_folder, output_file):

    combined_objects = []


    for file_name in os.listdir(input_folder):
        if file_name.endswith(".json"):
            input_file_path = os.path.join(input_folder, file_name)


            with open(input_file_path, 'r') as file:
                data = json.load(file)


            has_vehicle = False
            has_license_plate = False
            for obj in data["objects"]:
                class_title = obj["classTitle"].lower()
                if class_title == "vehicle":
                    has_vehicle = True
                elif class_title == "license plate":
                    has_license_plate = True


            if has_vehicle or has_license_plate:
                combined_objects.extend(data["objects"])


    combined_data = {
        "objects": combined_objects
    }


    for obj in combined_data["objects"]:
        if obj["classTitle"].lower() == "vehicle":
            obj["classTitle"] = "Car"
        elif obj["classTitle"].lower() == "license plate":
            obj["classTitle"] = "Number"


    with open(output_file, 'w') as file:
        json.dump(combined_data, file, indent=4)

    print(f"Combined and converted JSON saved as: {output_file}")
