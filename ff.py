import requests
import os

# Check availability of zip folder from URL
def check_zip_folder(url):
    response = requests.head(url)
    if response.status_code == 200:
        content_type = response.headers.get('content-type')
        if content_type == 'application/zip':
            print(f"{url} is a valid ZIP folder")
        else:
            print(f"{url} is not a ZIP folder")
    else:
        print(f"{url} is not available")

# Check for existence of files in a folder
def check_folder_files(folder_path, file_names_path):
    with open(file_names_path, 'r') as f:
        file_names = f.read().splitlines()
    for file_name in file_names:
        file_path = os.path.join(folder_path, file_name)
        if os.path.exists(file_path):
            print(f"{file_name} exists in {folder_path}")
        else:
            print(f"{file_name} does not exist in {folder_path}")

# Example usage
zip_url = 'https://example.com/example.zip'
check_zip_folder(zip_url)

folder_path = '/path/to/folder'
file_names_path = '/path/to/file_names.txt'
check_folder_files(folder_path, file_names_path)
