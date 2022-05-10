import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class Parser(object):
    """
    Base class for all parsers.
    """

    def __init__(self, filename):
        """
        Initialize the parser.
        """
        self.filename = filename
        self.file = None
        self.line_number = 0
        self.line = None
        self.line_length = 0
        self.line_position = 0
        self.line_remaining = None
        self.line_remaining_length = 0
        self.line_remaining_position = 0
        self.line_remaining_start = 0
        self.line_remaining_end = 0

    def __del__(self):
        """
        Finalize the parser.
        """
        self.close()

    def open(self):
        """
        Open the file.
        """
        self.file = codecs.open(self.filename, 'r', 'utf-8', 'strict')

    def close(self):
        """
        Close
