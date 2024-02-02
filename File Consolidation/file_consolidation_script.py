import os
import shutil

def move_files_to_single_folder(source_dir, target_dir):
    """ Move all files from subdirectories of source_dir to target_dir """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, dirs, files in os.walk(source_dir):
        for file_ in files:
            # Construct the full file path
            file_path = os.path.join(root, file_)
            # Construct the target file path
            target_file_path = os.path.join(target_dir, file_)

            # Rename the file if a file with the same name exists in the target directory
            base, extension = os.path.splitext(file_)
            counter = 1
            while os.path.exists(target_file_path):
                target_file_path = os.path.join(target_dir, f"{base}_{counter}{extension}")
                counter += 1

            # Move the file
            shutil.move(file_path, target_file_path)

# Directory containing the subdirectories and files
source_directory = "<Your Source Directory Goes here>"
# Directory where all files will be moved to
target_directory = "<your target directory goes here>"

move_files_to_single_folder(source_directory, target_directory)
