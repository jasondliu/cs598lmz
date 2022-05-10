import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_contents(filename):
    """
    Returns the contents of the given file.
    """
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_list(directory):
    """
    Returns a list of files in a given directory.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory)]

def get_file_name(file_path):
    """
    Returns the name of a file, without the path or extension.
    """
    return os.path.splitext(os.path.basename(file_path))[0]

def get_file_extension(file_path):
    """
    Returns the extension of a file.
    """
    return os.path.splitext(file_path)[1]

def get_file_name_extension(file_path):
    """
    Returns the name and extension of
