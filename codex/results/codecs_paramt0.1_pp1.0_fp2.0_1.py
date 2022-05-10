import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
#  Functions
#
#------------------------------------------------------------------------------

def get_file_list(path, ext):
    """
    Returns a list of files with the given extension in the given path.
    """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(ext)]

def get_file_list_recursive(path, ext):
    """
    Returns a list of files with the given extension in the given path and its
    subdirectories.
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.endswith(ext):
                file_list.append(os.path.join(root, f))
    return file_list

def get_file_list_recursive_with_path(path, ext):
    """
    Returns a list of files with the given extension in the given path and its
    subdirectories.
    """

