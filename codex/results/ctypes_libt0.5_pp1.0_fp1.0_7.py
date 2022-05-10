import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# Loop through all the files in the current working directory.
for filename in os.listdir("."):
    # Ignore directories, just process files
    if os.path.isdir(filename):
        continue

    new_name = get_fixed_filename(filename)
    print("Renaming {} to {}".format(filename, new_name))

    # Option 1: rename file to new name - in place
    os.rename(filename, new_name)

    # Option 2: move file to new place, with new name
    # shutil.move(filename, "new/" + new_name)
