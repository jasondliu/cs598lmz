import lzma
lzma

# archive.py

import lzma

class CompressedFile:
    """
    A generic base class for working with
    compressed files.

    This class should not be instantiated directly,
    but through the subclasses defined below.
    """

    def __init__(self, filename):
        """
        Create a compressed file object.
        filename is the name of the compressed file.
        """
        self.filename = filename

    def __enter__(self):
        """
        Called when the user enters the 'with' statement.
        """
        self.file = lzma.open(self.filename, self.mode)
        return self

    def __exit__(self, type, value, traceback):
        """
        Called when the user exits the 'with' statement.
        """
        self.file.close()

    def read(self, size=None):
        """
        Read at most size uncompressed bytes from the file.

        If size is negative or omitted, read until EOF is reached.
        """
