import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

def get_file_content(file_path):
    """
    Reads the content of a file and returns it as a string.
    """
    with open(file_path, 'r') as f:
        return f.read()

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

def get_file_content_as_list(file_path):
    """
    Reads the content of a file and returns it as a list of strings.
    """
    with open(file_path, 'r') as f:
        return f.readlines()

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

def get_file_content_as_list_of_lines(file_path):
    """
    Reads the content of a file and returns it as a list of strings.
    """
    with open(file_path, 'r') as f:
        return f.read().splitlines()

#------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------

def get_file_content_as
