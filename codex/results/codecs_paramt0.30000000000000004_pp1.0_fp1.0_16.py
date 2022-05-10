import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_files_in_dir(dir_path):
    """
    Returns a list of all files in a directory.
    """
    files = []
    for file in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file)):
            files.append(file)
    return files

def get_files_in_dir_recursive(dir_path):
    """
    Returns a list of all files in a directory and its subdirectories.
    """
    files = []
    for root, dirs, file in os.walk(dir_path):
        for f in file:
            files.append(os.path.join(root, f))
    return files

def get_dirs_in_dir(dir_path):
    """
    Returns a list of all directories in a directory.
    """
    dirs = []
    for dir in os.listdir(dir_path):
        if os.path.isdir(os.path
