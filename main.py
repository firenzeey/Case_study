from reformat import reformat_json_files
from combine import combine_and_convert_json_files


def main():
    # Provide the paths to the input and output folders
    input_folder = "sampleJson"
    output_folder = "Modified files"

    reformat_json_files(input_folder, output_folder)

    output_combined_json = "Modified files\combined_file.json"

    combine_and_convert_json_files(input_folder, output_combined_json)

if __name__ == "__main__":
    main()

