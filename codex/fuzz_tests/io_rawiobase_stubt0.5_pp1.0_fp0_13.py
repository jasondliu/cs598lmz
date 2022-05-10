import io
class File(io.RawIOBase):
    """
    File(name: str, mode: str='r', buffering: int=-1, encoding: Optional[str]=None, errors: Optional[str]=None, newline: Optional[str]=None, closefd: bool=True, opener: Optional[Callable[[str, int], int]]=None)
    File(fd: int, mode: str='r', buffering: int=-1, encoding: Optional[str]=None, errors: Optional[str]=None, newline: Optional[str]=None, closefd: bool=True)
    """
    def close(self) -> None:
        """
        close() -> None.  Close the file.

        A closed file cannot be used for further I/O operations.  close() may be
        called more than once without error.
        """
        pass

    def fileno(self) -> int:
        """
        fileno() -> int
        Return the integer "file descriptor" that is used by the underlying
        implementation to request I/O operations from the operating system.
        """
        pass

    def flush(self) -> None:
       
