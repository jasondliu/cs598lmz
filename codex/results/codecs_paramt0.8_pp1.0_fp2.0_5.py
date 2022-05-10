import codecs
codecs.register_error('surrogate_escape', codecs.surrogateescape_error)

# -------------------------
# Exercise 3
# -------------------------
def does_directory_exist_with_name(dir_name):
    """
    The function does_directory_exist_with_name(dir_name) checks if a directory exists in the
    current directory.

    Parameters:
    - dir_name (string): the directory name.

    Return value:
    - True: if the directory exists.
    - False: if the directory does not exist.
    """
    return path.isdir(dir_name)

# -------------------------
# Exercise 4
# -------------------------
def copy_binaries(src, dest):
    """
    The function copy_binaries(src, dest) takes a source and a destination folder, then copies
    all the binary files from the source directory to the destination directory.

    Note: the function uses os.walk and os.listdir to iterate through the folders.

    Parameters:
    - src (string): the path to the source directory.
    - dest (string): the path
