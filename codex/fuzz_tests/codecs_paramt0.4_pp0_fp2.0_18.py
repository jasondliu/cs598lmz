import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class FileReader(object):
    """
    This class reads a file.
    """

    def __init__(self, file_name):
        """
        Constructor.
        """

        # initialize the file name
        self.file_name = file_name

        # initialize the file handle
        self.file_handle = None

    def __del__(self):
        """
        Destructor.
        """

        # close the file handle
        self.close()

    def open(self):
        """
        This method opens the file.
        """

        # open the file
        self.file_handle = codecs.open(self.file_name, 'r', 'utf-8', 'strict')

    def close(self):
        """
        This method closes the file.
        """

        # close the file handle
        if self.file_handle != None:
            self.file_handle.close()
            self.file_handle = None

    def read_line(self):

