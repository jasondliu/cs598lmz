import io
class File(io.RawIOBase):
    """File(name: str, mode: str = 'r', buffering: int = -1, encoding: Optional[str] = None, errors: Optional[str] = None, newline: Optional[Union[str, bytes]] = None, closefd: bool = True, opener: Optional[Callable[[int, str], int]] = None) -> FileIO

Open file and return a corresponding file object.

If the file cannot be opened, IOError is raised.

The mode can be 'r', 'w' or 'a' for reading (default),
writing or appending.  The file will be created if it doesn't exist
when opened for writing or appending; it will be truncated when
opened for writing.  Add a '+' to the mode to allow simultaneous
reading and writing.

'U' mode is deprecated and will raise an exception in future versions
of Python.  It has no effect in Python 3.0, which uses universal newlines
mode.

'b' appended to the mode opens the file in binary mode: now the data
is read and written in the form of bytes objects.  This mode
