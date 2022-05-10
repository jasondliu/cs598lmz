import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_encoding(file):
    """
    Get the encoding of a file.
    """
    with open(file, 'rb') as f:
        rawdata = f.read()
    encoding = chardet.detect(rawdata)['encoding']
    if encoding is None:
        encoding = 'utf-8'
    return encoding

def _get_lines(file):
    """
    Get all the lines of a file.
    """
    encoding = _get_encoding(file)
    with codecs.open(file, 'r', encoding=encoding, errors='strict') as f:
        lines = f.readlines()
    return lines

def _get_line_count(file):
    """
    Get the number of lines in a file.
    """
    return len(_get_lines(file))

def _get_line_lengths(file):
    """
    Get the length of each line in a file.
    """
    lines = _get_lines(file)
