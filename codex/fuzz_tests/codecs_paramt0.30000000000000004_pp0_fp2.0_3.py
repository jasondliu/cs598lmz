import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_names(path):
    """
    Returns a list with the file names in the directory specified by path.
    """
    file_names = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            file_names.append(file)
    return file_names


def get_file_content(path):
    """
    Returns the content of the file specified by path.
    """
    with codecs.open(path, 'r', 'utf-8', 'strict') as f:
        content = f.read()
    return content


def get_file_content_as_list(path):
    """
    Returns the content of the file specified by path as a list of lines.
    """
    with codecs.open(path, 'r', 'utf-8', 'strict') as f:
        content = f.readlines()
    return content


def get_file_content_as_list_of
