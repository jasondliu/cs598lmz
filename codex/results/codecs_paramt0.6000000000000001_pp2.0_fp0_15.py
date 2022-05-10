import codecs
codecs.register_error('strict', codecs.ignore_errors)


def read_file(filename, encoding='utf-8'):
    """
    Read the content of a utf-8 encoded file
    """
    try:
        with open(filename, 'r', encoding=encoding) as f:
            return f.read()
    except UnicodeDecodeError:
        return read_file(filename, encoding='ascii')


def list_files(directory):
    """
    List all files in a directory recursively
    """
    for root, _, files in os.walk(directory):
        for filename in files:
            yield os.path.join(root, filename)


def list_directories(directory):
    """
    List all directories in a directory recursively
    """
    for root, dirs, _ in os.walk(directory):
        for dirname in dirs:
            yield os.path.join(root, dirname)


def read_json(filename):
    """
    Load a json file and return its content
    """
    with open(filename
