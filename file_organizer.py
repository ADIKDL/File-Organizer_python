import os
import shutil


def create_folder_if_needed(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    return subfolder_path


def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = filename.split(".")[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_folder_if_needed(folder_path, subfolder_name)
                file_path = os.path.join(folder_path, filename)
                new_location = os.path.join(subfolder_path, filename)
                if not os.path.exists(new_location):
                    shutil.move(file_path, subfolder_path)
                else:
                    print("Already exists")


if __name__ == "__main__":
    print("Desktop Organiser Script")
    folder_path = ""  #provide the path of the location or folder in which you want to organize all the files 
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("cleaning complete")
    else:
        print("Invalid folder path")
