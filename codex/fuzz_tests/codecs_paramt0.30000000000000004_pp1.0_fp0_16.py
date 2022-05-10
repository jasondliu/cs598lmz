import codecs
codecs.register_error('ignore', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

def get_file_list(path):
    """
    Returns a list of files in the given path
    """
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def get_dir_list(path):
    """
    Returns a list of directories in the given path
    """
    return [os.path.join(path, f) for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

def get_file_list_recursive(path):
    """
    Returns a list of files in the given path and its subdirectories
    """
    file_list = []
    for dirname, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_list.append(os.path.join(dirname, filename))
    return
