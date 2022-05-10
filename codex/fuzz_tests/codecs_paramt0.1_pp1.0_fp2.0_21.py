import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
#  Functions
#
#------------------------------------------------------------------------------

def get_file_list(path):
    """
    Returns a list of files in the given path.
    """
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

def get_file_list_recursive(path):
    """
    Returns a list of files in the given path and its subdirectories.
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for f in files:
            file_list.append(os.path.join(root, f))
    return file_list

def get_file_list_recursive_with_ext(path, ext):
    """
    Returns a list of files in the given path and its subdirectories with the
    given extension.
    """
    file_list = []
    for root, dirs, files in os.walk(path):
       
