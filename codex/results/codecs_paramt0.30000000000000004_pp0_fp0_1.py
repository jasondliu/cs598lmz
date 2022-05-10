import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_encoding(fileobj):
    """
    Return the encoding of a file.
    """
    # Read the first two lines
    first_lines = fileobj.readlines(2)
    fileobj.seek(0)
    # Get the encoding from the first line
    encoding = re.search(r'^#.*coding[:=][\s]*([-\w.]+)', first_lines[0])
    if encoding:
        return encoding.group(1)
    # Get the encoding from the second line
    encoding = re.search(r'^#.*coding[:=][\s]*([-\w.]+)', first_lines[1])
    if encoding:
        return encoding.group(1)
    # Default to utf-8
    return 'utf-8'

def _get_source(fileobj):
    """
    Return the source code of a file.
    """
    # Get the encoding
    encoding = _get_encoding(fileobj)
    # Read
