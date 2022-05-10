import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

def get_file_list(path):
    """
    Returns a list of files in a directory.
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

#-------------------------------------------------------------------------------

def get_file_list_pattern(path, pattern):
    """
    Returns a list of files in a directory matching a pattern.
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if fnmatch.fnmatch(file, pattern):
                file_list.append(os.path.join(root, file))
    return file_list

#-------------------------------------------------------------------------------

def get_file_list_regex(path, regex):
    """
    Returns a list of files in a directory matching a regular expression.
    """
    file_list = []
   
