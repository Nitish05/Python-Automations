# File Management Scripts

This repository contains two powerful Python scripts designed to aid in file management tasks: one for consolidating files from various subdirectories into a single directory, and another for sorting files within a directory into folders based on their file extensions. These scripts are invaluable tools for organizing files and directories efficiently.

## Scripts Overview

### File Consolidation Script

- **Purpose**: Moves all files from subdirectories within a specified source directory to a single target directory.
- **Features**:
  - Deep directory traversal.
  - Automatic conflict resolution by renaming duplicate filenames.
  - Simplifies file organization by consolidating files into one location.

### File Sorting Script

- **Purpose**: Sorts files in a given directory into folders based on their file extensions.
- **Features**:
  - Automatic sorting into extension-named folders.
  - Works recursively through all levels of subdirectories.
  - Streamlines the organization of files by type.

## Getting Started

### Prerequisites

Both scripts require Python to be installed on your system. They are compatible with Python 3.x versions.

### Installation

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/Nitish05/Python-Automations.git
```

## Configuration and Usage
### File Consolidation Script
1. Open file_consolidation_script.py in a text editor.
2. Set source_directory and target_directory with the paths to your desired source and target directories.
```python
source_directory = "<Your Source Directory Goes Here>"
target_directory = "<Your Target Directory Goes Here>"
```
### Run the script:
```bash
python file_consolidation_script.py
```
### File Sorting Script
1. Open file_sorting_script.py in a text editor.
2. Set path to the directory you wish to organize:
```python
path = "<Your File Path Goes Here>"
```
### Run the script:
```bash
python file_sorting_script.py
```
## How It Works
The File Consolidation Script moves files from multiple subdirectories into a single directory, renaming duplicates when necessary.
The File Sorting Script organizes files into folders named after their extensions, operating both on the main directory and its subdirectories.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
Please ensure you have backups of your data before running these scripts, especially when organizing important files. The authors take no responsibility for lost or incorrectly sorted files due to script execution.

## Support
If you encounter any issues or have questions, please file an issue on the GitHub project page. We're here to help.
