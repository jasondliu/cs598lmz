import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_list(path):
    """
    Get all files in a directory
    """
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    return files

def get_file_list_recursive(path):
    """
    Get all files in a directory and subdirectories
    """
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
    return files

def get_file_list_recursive_with_path(path):
    """
    Get all files in a directory and subdirectories
    """
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))
    return files

def get_dir_list(path):
