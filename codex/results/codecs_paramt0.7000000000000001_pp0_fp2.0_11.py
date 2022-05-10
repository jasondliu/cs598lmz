import codecs
codecs.register_error('ignore', codecs.lookup('utf-8'))


def read_file(path, encoding='utf-8'):
    """Read a file in UTF-8."""
    with codecs.open(path, 'r', encoding=encoding) as f:
        return f.read()


def read_file_ignore(path, encoding='utf-8'):
    """Read a file in UTF-8 and magically ignore errors."""
    with codecs.open(path, 'r', encoding=encoding, errors='ignore') as f:
        return f.read()


def write_file(path, data, encoding='utf-8'):
    """Write a file in UTF-8."""
    with codecs.open(path, 'w', encoding=encoding) as f:
        f.write(data)


def read_lines(path, encoding='utf-8'):
    """Yield lines from a file in UTF-8."""
    with codecs.open(path, 'r', encoding=encoding) as f:
        for line in f:
           
