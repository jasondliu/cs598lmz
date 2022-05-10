import codecs
codecs.register_error('strict', codecs.ignore_errors)

def read_file(filename):
    """
    Reads a file and returns its contents as a string.
    """
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

def write_file(filename, string):
    """
    Writes a string to a file.
    """
    with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
        f.write(string)

def get_files(directory, extension):
    """
    Returns a list of all files in a directory with a given extension.
    """
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]

def get_files_recursive(directory, extension):
    """
    Returns a list of all files in a directory and its subdirectories with a given extension.
    """
    files = []
    for root, dirnames, filenames
