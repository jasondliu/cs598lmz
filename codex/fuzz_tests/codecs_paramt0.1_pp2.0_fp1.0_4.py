import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
# 
#

def get_file_list(path):
    """
    Returns a list of files in the given path.
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_file_list_recursive(path):
    """
    Returns a list of files in the given path.
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def get_file_list_recursive_with_ext(path, ext):
    """
    Returns a list of files in the given path.
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
