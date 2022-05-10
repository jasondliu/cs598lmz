import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_all_files(dir_path):
    """
    Get all files in a directory
    """
    return [os.path.join(dir_path, f) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]

def get_all_dirs(dir_path):
    """
    Get all directories in a directory
    """
    return [os.path.join(dir_path, f) for f in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, f))]

def get_all_files_recursive(dir_path):
    """
    Get all files in a directory recursively
    """
    return [os.path.join(dir_path, f) for f in os.listdir(dir_path)] + [os.path.join(dir_path, f) for f in os.listdir(dir_path) if os.path.
