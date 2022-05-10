import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
#  Functions
#
#------------------------------------------------------------------------------

def get_file_path(filename):
    """
    Returns the absolute path to a file, whether it's in the current directory
    or in the "data" subdirectory.
    """
    try:
        data_path = os.path.join(os.path.dirname(__file__), "data", filename)
        with open(data_path):
            return data_path
    except IOError:
        return filename

def get_data_path(path):
    """
    Returns the absolute path to a data file, whether it's in the current
    directory or in the "data" subdirectory.
    """
    return get_file_path(os.path.join("data", path))

def get_data_file(path):
    """
    Returns a file object for a data file, whether it's in the current
    directory or in the "data" subdirectory.
    """
    return open(get_data_path(path), "rb
