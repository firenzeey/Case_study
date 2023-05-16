import os
import json

def reformat_json_files(input_folder, output_folder):

    os.makedirs(output_folder, exist_ok=True)


    for file_name in os.listdir(input_folder):
        if file_name.endswith(".json"):
            input_file_path = os.path.join(input_folder, file_name)


            with open(input_file_path, 'r') as file:
                data = json.load(file)


            has_vehicle = False
            has_license_plate = False


            if "objects" in data:
                for item in data["objects"]:
                    if "classTitle" in item:
                        class_title = item["classTitle"].lower()
                        if class_title == "vehicle":
                            has_vehicle = True
                        elif class_title == "license plate":
                            has_license_plate = True


            if has_vehicle or has_license_plate:

                output_file_name = "formatted_" + file_name
                output_file_path = os.path.join(output_folder, output_file_name)


                with open(output_file_path, 'w') as file:
                    json.dump(data, file, indent=4)

                print(f"Reformatted JSON saved as: {output_file_path}")
            else:
                print(f"Ignored file: {file_name} (missing required classes)")