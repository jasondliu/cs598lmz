import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------

class File(object):
    """
    File object.
    """

    def __init__(self, path, mode='r', encoding='utf-8', errors='strict'):
        """
        Constructor.
        """
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.file = None

    def __enter__(self):
        """
        Open the file.
        """
        self.file = codecs.open(self.path, self.mode, self.encoding, self.errors)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Close the file.
        """
        self.file.close()
        self.file = None

    def __iter__(self):
        """
        Iterate over the file.
        """
        return self

    def __next__(self):
        """
        Read
