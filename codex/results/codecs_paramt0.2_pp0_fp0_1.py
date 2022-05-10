import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_list(path):
    """
    Get the list of files in a directory.
    """
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def get_dir_list(path):
    """
    Get the list of directories in a directory.
    """
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

def get_file_name(path):
    """
    Get the file name from a path.
    """
    return os.path.basename(path)

def get_file_ext(path):
    """
    Get the file extension from a path.
    """
    return os.path.splitext(path)[1]

def get_file_name_no_ext(path):
    """
    Get the
