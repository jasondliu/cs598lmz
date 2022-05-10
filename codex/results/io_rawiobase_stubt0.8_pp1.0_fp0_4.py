import io
class File(io.RawIOBase):
    """Base class for file objects."""

    name = None
    """file names passed to open() are accessible in this attribute."""

    mode = None
    """mode argument passed to open(). One of 'r', 'w', 'x', 'a', 'b', 't', '+' """

    closed = True
    """True iff file is closed."""

    def close(self):
        """close the file.
        close() may be called more than once without error.
        """
        pass

    @classmethod
    def open(cls, name, mode='r', buffering=-1, **kwargs):
        """Open file and return a corresponding file object.

        If the file cannot be opened, an OSError is raised.

        *name* is the file name passed to the builtin open() function.

        *mode* is the string indicating how the file will be used.
        It is the string argument passed to open() after any leading character
        used to indicate binary or text mode (e.g. 'b' or 't'). The default is 'r'.

        *buffering
