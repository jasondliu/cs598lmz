import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

def get_file_contents(filename):
    """
    Returns the contents of a file as a string.
    """
    with open(filename, 'r') as f:
        return f.read()

#-------------------------------------------------------------------------------

def get_file_lines(filename):
    """
    Returns the contents of a file as a list of lines.
    """
    with open(filename, 'r') as f:
        return f.readlines()

#-------------------------------------------------------------------------------

def get_file_lines_as_list(filename):
    """
    Returns the contents of a file as a list of lines.
    """
    with open(filename, 'r') as f:
        return list(f)

#-------------------------------------------------------------------------------

def get_file_lines_as_set(filename):
    """
    Returns the contents of a file as a set of lines.
    """
    with open(filename, 'r') as f:
        return set(f)

#-------------------------------------------------------------------------------

def get_file_lines
