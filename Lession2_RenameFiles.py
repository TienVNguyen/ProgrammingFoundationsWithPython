import os

def rename_files():
    # Get all files
    files = os.listdir(r"/Users/tiennguyen/Desktop/prank")
    print(files)
    os.chdir("/Users/tiennguyen/Desktop/prank")
    path = os.getcwd()
    print(path)

    # Rename files
    for file in files:
        os.rename(file, file.translate(None, "0123456789"))

rename_files()
