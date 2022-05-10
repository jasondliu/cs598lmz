import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
#  FUNCTIONS
#
#------------------------------------------------------------------------------

def get_file_path(file_name):
    """
    Returns the path to a file in the data directory.

    :param file_name: name of the file
    :type file_name: str
    :return: path to the file
    :rtype: str
    """
    return os.path.join(os.path.dirname(__file__), 'data', file_name)

def get_file_content(file_name):
    """
    Returns the content of a file in the data directory.

    :param file_name: name of the file
    :type file_name: str
    :return: content of the file
    :rtype: str
    """
    with codecs.open(get_file_path(file_name), 'r', 'utf-8', 'strict') as f:
        return f.read()

def get_file_content_as_lines(file_name):
    """

