import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

def read_file(filename):
    """
    Reads the contents of a file.
    """
    try:
        with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
            return f.read()
    except IOError:
        return None

#-------------------------------------------------------------------------------

def write_file(filename, content):
    """
    Writes the contents of a file.
    """
    try:
        with codecs.open(filename, 'w', 'utf-8', 'strict') as f:
            f.write(content)
    except IOError:
        return False
    return True

#-------------------------------------------------------------------------------

def get_file_content(filename):
    """
    Get the content of a file.
    """
    try:
        with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
            content = f.read()
    except IOError:
        content = None
    return content

#
