import codecs
codecs.register_error('strict', codecs.ignore_errors)

# TODO: make this a class

# TODO: make this a class

def get_file_list(path, file_type):
    """
    Returns a list of files of a given type in a given directory
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(file_type):
                file_list.append(os.path.join(root, file))
    return file_list


def get_file_list_with_prefix(path, file_type, prefix):
    """
    Returns a list of files of a given type in a given directory
    """
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(file_type) and file.startswith(prefix):
                file_list.append(os.path.join(root, file))
    return file_list


def get
