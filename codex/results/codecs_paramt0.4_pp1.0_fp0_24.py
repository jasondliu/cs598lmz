import codecs
codecs.register_error('strict', codecs.ignore_errors)

def get_file_encoding(path):
    """
    Returns the encoding of the given file.
    """
    with open(path, 'rb') as f:
        rawdata = f.read()
    return chardet.detect(rawdata)['encoding']

def get_file_content(path):
    """
    Returns the content of the given file.
    """
    with codecs.open(path, 'r', encoding=get_file_encoding(path), errors='strict') as f:
        return f.read()

def get_file_content_as_lines(path):
    """
    Returns the content of the given file as a list of lines.
    """
    with codecs.open(path, 'r', encoding=get_file_encoding(path), errors='strict') as f:
        return f.readlines()

def get_file_content_as_json(path):
    """
    Returns the content of the given file as a json object.
    """

