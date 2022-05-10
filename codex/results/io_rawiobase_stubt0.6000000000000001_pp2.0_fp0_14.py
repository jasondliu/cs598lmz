import io
class File(io.RawIOBase):
    """File(name: str, mode: str = "r")

    Open a file.

    The mode can be 'r', 'w', 'x' or 'a' for reading (default), writing,
    exclusive creation or appending.  The file will be created if it doesn't
    exist when opened for writing or appending; it will be truncated when
    opened for writing.  Add a 'b' to the mode for binary files.
    Add a '+' to the mode to allow simultaneous reading and writing.
    If the mode is omitted, 'r' is assumed.

    Opening a file with 'x' mode fails if the file already exists.
    """
    def __init__(self, name, mode='r'):
        pass

    def name(self):
        """Return the file's name"""
        return ""

    def mode(self):
        """Return the file's mode"""
        return ""

    def closed(self):
        """Return True if the file is closed"""
        return False

    def close(self):
        """Close the file"""
        return 0

    def fil
