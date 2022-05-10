import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

def get_file_contents(filename):
    """
    Read the contents of a file.
    """
    with open(filename, 'r') as f:
        return f.read()

#-------------------------------------------------------------------------------

def get_file_contents_utf8(filename):
    """
    Read the contents of a file in UTF-8.
    """
    with codecs.open(filename, 'r', 'utf-8', 'strict') as f:
        return f.read()

#-------------------------------------------------------------------------------

def get_file_contents_utf8_bom(filename):
    """
    Read the contents of a file in UTF-8 with BOM.
    """
    with codecs.open(filename, 'r', 'utf-8-sig', 'strict') as f:
        return f.read()

#-------------------------------------------------------------------------------

def get_file_contents_utf16(filename):
    """
    Read the contents of a file in UTF-16.
    """
    with
