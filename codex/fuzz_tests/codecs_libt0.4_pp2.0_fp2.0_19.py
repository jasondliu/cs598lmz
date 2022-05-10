import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# ################################################################################################################################

# ################################################################################################################################

def get_file_list(path):
    """
    Get a list of all files in a directory.

    Args:
        path (str): Path to a directory.
    Returns:
        list: List of file names.
    """
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# ################################################################################################################################

# ################################################################################################################################

def get_dir_list(path):
    """
    Get a list of all directories in a directory.

    Args:
        path (str): Path to a directory.
    Returns:
        list: List of directory names.
    """
    return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
