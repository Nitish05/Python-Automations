import os
import shutil

def move_file(file_path, extension, root):
    """ Move file to its respective extension directory """
    ext_dir = os.path.join(root, extension)
    if not os.path.exists(ext_dir):
        os.makedirs(ext_dir)
    shutil.move(file_path, os.path.join(ext_dir, os.path.basename(file_path)))

def sort_files_in_directory(directory_path):
    """ Sort files in the given directory into folders by extension """
    for root, dirs, files in os.walk(directory_path):
        for file_ in files:
            # Extract the file extension
            _, ext = os.path.splitext(file_)
            ext = ext[1:].lower()
            if ext:
                move_file(os.path.join(root, file_), ext, directory_path)

# Path of the directory to be sorted
path = "<Your File path goes Here>"
sort_files_in_directory(path)
