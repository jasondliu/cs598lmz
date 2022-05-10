import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class File:
    """
    File class.
    """

    def __init__(self, file_name, mode='r', encoding='utf-8'):
        """
        Constructor.
        """

        # initialize the file name
        self.file_name = file_name

        # initialize the file mode
        self.mode = mode

        # initialize the file encoding
        self.encoding = encoding

        # initialize the file
        self.file = None

    #---------------------------------------------------------------------------

    def open(self):
        """
        Open the file.
        """

        # open the file
        self.file = codecs.open(self.file_name, self.mode, self.encoding, 'strict')

    #---------------------------------------------------------------------------

    def close(self):
        """
        Close the file.
        """

        # close the file
        self.file.close()

    #---------------------------------------------------------------------------

    def read(self):
        """
        Read the file.
        """

        # read the file

