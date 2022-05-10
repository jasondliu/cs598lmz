import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_encoding(file_path):
    """
    Get the encoding of a file.
    """
    with open(file_path, 'rb') as f:
        rawdata = f.read()
    return chardet.detect(rawdata)['encoding']

def _get_file_content(file_path):
    """
    Get the content of a file.
    """
    with codecs.open(file_path, 'r', encoding=_get_encoding(file_path), errors='strict') as f:
        return f.read()

def _get_file_content_as_list(file_path):
    """
    Get the content of a file as a list.
    """
    with codecs.open(file_path, 'r', encoding=_get_encoding(file_path), errors='strict') as f:
        return f.readlines()

def _get_file_content_as_list_without_newline(file_path):
    """
