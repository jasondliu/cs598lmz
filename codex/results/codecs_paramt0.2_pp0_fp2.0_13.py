import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_all_files(path, ext):
    """
    Returns a list of all files in the given path with the given extension.
    """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(ext)]

def get_all_files_recursive(path, ext):
    """
    Returns a list of all files in the given path with the given extension.
    """
    all_files = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(ext):
                all_files.append(os.path.join(root, f))
    return all_files

def get_all_files_recursive_with_path(path, ext):
    """
    Returns a list of all files in the given path with the given extension.
    """
    all_files = []
    for root, dirs, files in os.walk(path):
        for f in files
