import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_encoding(file_path):
    """
    Get the encoding of a file.
    """
    with open(file_path, 'rb') as f:
        rawdata = f.read()
    return chardet.detect(rawdata)['encoding']

def _get_file_contents(file_path):
    """
    Get the contents of a file.
    """
    encoding = _get_encoding(file_path)
    with codecs.open(file_path, 'r', encoding=encoding, errors='strict') as f:
        return f.read()

def _get_file_lines(file_path):
    """
    Get the lines of a file.
    """
    encoding = _get_encoding(file_path)
    with codecs.open(file_path, 'r', encoding=encoding, errors='strict') as f:
        return f.readlines()

def _get_file_size(file_path):
    """

