import os
import shutil

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist.")
        return

    files_moved = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Skip folders
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()

            if not extension:
                category = "Others"
            else:
                category = extension[1:].upper() + " Files"

            destination_folder = os.path.join(folder_path, category)
            os.makedirs(destination_folder, exist_ok=True)

            # Move the file into its category folder
            shutil.move(
                file_path,
                os.path.join(destination_folder, filename)
            )

            files_moved += 1
            print(f"Moved: {filename} -> {category}")

    print(f"\nOrganization complete! {files_moved} files sorted.")


print("==========================")
print("     FILE ORGANIZER")
print("==========================")

folder = input("Enter the folder path to organize: ").strip()
organize_files(folder)