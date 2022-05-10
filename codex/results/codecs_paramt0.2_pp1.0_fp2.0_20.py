import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

def get_file_content(file_name):
    """
    Get the content of a file.
    """
    with codecs.open(file_name, 'r', 'utf-8', 'strict') as file:
        return file.read()

#-------------------------------------------------------------------------------

def get_file_content_as_list(file_name):
    """
    Get the content of a file as a list of lines.
    """
    with codecs.open(file_name, 'r', 'utf-8', 'strict') as file:
        return file.readlines()

#-------------------------------------------------------------------------------

def get_file_content_as_list_of_strings(file_name):
    """
    Get the content of a file as a list of strings.
    """
    with codecs.open(file_name, 'r', 'utf-8', 'strict') as file:
        return file.read().splitlines()

#-------------------------------------------------------------------------------

def get_file_content_as_list_
