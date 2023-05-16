Run main.py to execute the scripts for both of the scenario.

Scenario 1: JSON File Formatting

Objective: Convert the JSON file format into a standard format.

1.The script will process each JSON file in the input folder.

2.If either "Vehicle" or "License plate" class is present, the script will convert the JSON file to the standard format and save it as "formatted_pos_0.png.json" (or a similar name based on the original file).

3.If both "Vehicle" and "License plate" classes are missing, the script will create a formatted JSON file based on the example file "formatted_pos_10492.png.json".

4.The formatted JSON files will be saved in the output folder.


Scenario 2: JSON File Combination and Class Name Change.

Objective: Combine multiple JSON files into a single JSON file and change the class names "Vehicle" to "Car" and "License plate" to "Number" in the combined file.

1.The script will process each JSON file in the input folder.

2.It will combine the JSON files into a single JSON file, preserving the objects from each file.

3.If a JSON object has the class name "Vehicle", it will be changed to "Car" in the combined JSON file.

4.If a JSON object has the class name "License plate", it will be changed to "Number" in the combined JSON file.

5.The combined JSON file will be saved as "combined.json" (or a similar name) in the specified output location.

