import codecs
codecs.register_error('strict', codecs.ignore_errors)

# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------

def get_file_content(file_path):
    """
    Return the content of the file.
    """
    with codecs.open(file_path, 'r', 'utf-8', 'strict') as f:
        return f.read()

# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------

def get_file_content_as_list(file_path):
    """
    Return the content of the file as a list of lines.
    """
    with codecs.open(file_path, 'r', 'utf-8', 'strict') as f:
        return f.readlines()

# ------------------------------------------------------------------------------
#
# ------------------------------------------------------------------------------

def get_file_content_as_list_of_words(file_path):
    """
    Return the content of the file as a list of words.
    """
    with codecs.open(file_path, 'r', 'utf-8', 'strict') as f:
        return f.read().split()

