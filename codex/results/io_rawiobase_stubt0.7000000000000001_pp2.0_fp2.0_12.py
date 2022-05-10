import io
class File(io.RawIOBase):
    """File(name: str, mode: str = 'r', buffering: int = -1, encoding: str = None, errors: str = None, newline: str = None, closefd: bool = True, opener: Optional[Callable[[str, int], int]] = None)

    Open a file.

    The first two arguments are the same as for stdio's fopen():
    name is the file name to be opened, and mode is a string indicating
    how the file is to be opened. Accepts the same values as the builtin
    open() function.
    
    The most commonly-used values of mode are 'r' for reading, 'w' for
    writing (truncating the file if it already exists), and 'a' for appending
    (which on some Unix systems means that all writes append to the end of the
    file regardless of the current seek position). If mode is omitted, it
    defaults to 'r'.
    
    The default is to use text mode, which may convert '\\n' line endings
    (the default on Unix systems) to a platform-specific representation on
    writing
