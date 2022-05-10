import codecs
codecs.register_error('strict', codecs.ignore_errors)

class File(object):
    """
    A class for reading from and writing to files.
    """

    def __init__(self, filename, mode='r', encoding=None):
        """
        Constructor.

        @param filename: the name of the file
        @type filename: string
        @param mode: the mode in which the file is opened
        @type mode: string
        @param encoding: the encoding of the file
        @type encoding: string
        """

        self.filename = filename
        self.mode = mode
        self.encoding = encoding

        if self.mode == 'r':
            self.file = codecs.open(self.filename, self.mode, self.encoding, 'strict')
        else:
            self.file = codecs.open(self.filename, self.mode, self.encoding)

    def __iter__(self):
        """
        Iterator.
        """

        return self

    def next(self):
        """
        Returns the next line from the file.

