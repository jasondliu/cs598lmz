import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
#  Functions
#
#------------------------------------------------------------------------------

def get_file_list(path, ext):
    """
    Returns a list of files in the given path with the given extension.
    """
    files = []
    for file in os.listdir(path):
        if file.endswith(ext):
            files.append(file)
    return files

def get_file_content(file):
    """
    Returns the content of the given file.
    """
    with open(file, 'r') as f:
        return f.read()

def get_file_content_encoded(file):
    """
    Returns the content of the given file encoded in utf-8.
    """
    with codecs.open(file, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_content_lines(file):
    """
    Returns the content of the given file as a list of lines.
    """
    with open
