import os
from datetime import datetime

# Directory containing the markdown files
dir_path = "/home/shivam/Work/0xdroidan.github.io/_posts"

# Traverse all files in the directory
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(".md"):  # Only rename markdown files
            # Construct the old file path
            old_file_path = os.path.join(root, file)
            
            # Construct the new file name with today's date as prefix
            new_file_name = f"{"2024-12-23"}-{file}"
            new_file_path = os.path.join(root, new_file_name)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_file_path} -> {new_file_path}")

