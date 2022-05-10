import io
class File(io.RawIOBase):
    """Base class for files.

    This class implements a file object.  To open a file, use the built-in
    open() function.

    This is an abstract class; you must derive from it and add implementation.

    Methods follow the standard file object API of Python 3.0.

    The constructor sets data attributes.  A subclass may add others.

    name
        The name of the file; always a str or None

    mode
        The I/O mode for the file; one of 'r', 'w', 'a' or 'x'.

    closed
        Boolean indicating whether the file is closed
    """

    # On Windows, importing os is needed for file flags
    if os.name == 'nt':
        import os

    # Binary files are supposed to have no newlines
    newlines = None

    def __init__(self, file, mode="r", closefd=True, opener=None):
        if type(file) is int:
            self._raw = _FileIO(file, (mode.replace("b", "")))
        else: self._raw = _FileIO(file, mode
