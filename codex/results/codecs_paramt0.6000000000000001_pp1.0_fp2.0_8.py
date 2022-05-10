import codecs
codecs.register_error('replace_with_space', codecs.lookup_error('ignore'))

def _get_dir_path(dirname):
    """Get the full path to dirname in the data directory."""
    return os.path.join(os.path.dirname(__file__), 'data', dirname)

def _get_file_path(filename):
    """Get the full path to filename in the data directory."""
    return os.path.join(os.path.dirname(__file__), 'data', filename)

def _get_data_file_handle(filename):
    """Get a handle to filename. If filename is a file in the data directory
    then return a handle to that. Otherwise, try to find the corresponding
    file in the data directory and return a handle to that.
    """
    if os.path.isfile(filename):
        return open(filename, 'r')

    filename = _get_file_path(filename)
    if os.path.isfile(filename):
        return open(filename, 'r')

    raise IOError("No such file
