import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_paths(dir_path, file_extension):
    """
    Get all file paths in a directory with a given extension.
    """
    file_paths = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(file_extension):
                file_paths.append(os.path.join(root, file))
    return file_paths

def get_file_names(dir_path, file_extension):
    """
    Get all file names in a directory with a given extension.
    """
    file_names = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(file_extension):
                file_names.append(file)
    return file_names

def get_file_name(file_path):
    """
    Get the name of a file from its path.
    """
   
