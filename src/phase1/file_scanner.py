from pathlib import Path

def scan_folder(folder_path):
    folder = Path(folder_path)

    if not folder:
        print("Folder does not exist!")
        return
    
    if not folder.is_dir():
        print("Path is not a folder.")
        return

    files = []

    for item in folder.iterdir():
        if item.is_file():
            files.append(item.name)

    print(f"Found {len(files)} file(s):")
    for file in files:
        print(f"- {file}")

scan_folder("data")