import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class File(object):
    """
    File object.
    """

    def __init__(self, file_path):
        """
        Constructor.

        @param file_path File path.
        """

        # initialize attributes
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.file_extension = os.path.splitext(file_path)[1]
        self.file_size = os.path.getsize(file_path)

    def __str__(self):
        """
        Returns the string representation of the class.

        @return String representation of the class.
        """

        return "File: {0}".format(self.file_path)

    def __repr__(self):
        """
        Returns the string representation of the class.

        @return String representation of the class.
        """

        return "File('{0}')".format(self.file_path)

    def
