import io
class File(io.RawIOBase):
    """File(name: str, mode: str = 'r', buffering: int = -1, encoding: Optional[str] = None, errors: Optional[str] = None, newline: Optional[str] = None, closefd: bool = True)
    
    Open a file, returning an object of the file type described in
    section :ref:`bltin-file-objects`.
    
    The mode can be 'r', 'w' or 'a' for reading (default), writing or
    appending.  The file will be created if it doesn't exist when opened
    for writing or appending; it will be truncated when opened for
    writing.  Add a 'b' to the mode for binary files.  Add a '+' to the
    mode to allow simultaneous reading and writing.  If the buffering
    argument is given, 0 means unbuffered, 1 means line buffered, and
    larger numbers specify the buffer size.  The preferred way to open a
    file is with the builtin :func:`open` function.
    
    'U' mode is deprecated and will raise an exception in
