import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
# 
#

def get_file_content(file_path):
    """
    Read the content of a file.
    """
    with codecs.open(file_path, 'r', encoding='utf-8', errors='strict') as f:
        return f.read()

def get_file_content_as_list(file_path):
    """
    Read the content of a file as a list of lines.
    """
    with codecs.open(file_path, 'r', encoding='utf-8', errors='strict') as f:
        return f.readlines()

def get_file_content_as_list_of_words(file_path):
    """
    Read the content of a file as a list of words.
    """
    with codecs.open(file_path, 'r', encoding='utf-8', errors='strict') as f:
        return f.read().split()

def get_file_content_as_list_of_words_and_p
