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
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(ext)]

def get_file_name(path):
    """
    Returns the file name of the given path.
    """
    return os.path.splitext(os.path.basename(path))[0]

def get_file_ext(path):
    """
    Returns the file extension of the given path.
    """
    return os.path.splitext(os.path.basename(path))[1]

def get_file_path(path):
    """
    Returns the file path of the given path.
    """
    return os.path.dirname(path)

def get_file_size(path):
    """
    Returns the
