import lzma
lzma.LZMA_PRESET_DEFAULT = 9

def _get_file_path(file_path):
    """
    Returns the file path with Python version appended, if the file path does not exist.
    """
    if os.path.isfile(file_path):
        return file_path
    else:
        return file_path + '.' + sys.version[0:3]


def _get_project_path(path):
    """
    Returns the project path, prepending the current working directory
    """
    if path.startswith('/'):
        return path
    else:
        return os.path.join(os.getcwd(), path)


def _make_parent_directory(file_path):
    """
    Make the parent directory for the specified file path.
    """
    parent_path = os.path.dirname(file_path)
    if not os.path.isdir(parent_path):
        os.makedirs(parent_path)


