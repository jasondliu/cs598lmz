import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
#  Functions
#
#------------------------------------------------------------------------------

def get_file_list(dir_path):
    """
    Returns a list of files in a directory.
    """
    file_list = []
    for file_name in os.listdir(dir_path):
        file_list.append(os.path.join(dir_path, file_name))
    return file_list

def get_file_list_recursive(dir_path):
    """
    Returns a list of files in a directory and its subdirectories.
    """
    file_list = []
    for dir_path, dir_names, file_names in os.walk(dir_path):
        for file_name in file_names:
            file_list.append(os.path.join(dir_path, file_name))
    return file_list

def get_file_name(file_path):
    """
    Returns the file name from a file path.
    """
    return os.path.basename(
