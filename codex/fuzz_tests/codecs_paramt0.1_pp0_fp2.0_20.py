import codecs
codecs.register_error('strict', codecs.ignore_errors)

#------------------------------------------------------------------------------
#
class File(object):
    """
    A file-like object that can be used as a context manager.
    """

    def __init__(self, path, mode='r', encoding='utf-8', errors='strict'):
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.errors = errors

    def __enter__(self):
        self.file = codecs.open(self.path, self.mode, self.encoding, self.errors)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

#------------------------------------------------------------------------------
#
def read_file(path, mode='r', encoding='utf-8', errors='strict'):
    """
    Read the contents of a file.
    """
    with File(path, mode, encoding, errors) as f:
        return f.read()

#------------------------------------------------------------------------------
#
def write_file(path
