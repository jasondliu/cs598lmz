import io
class File(io.RawIOBase):
    """
    File(name: str, mode: str = 'r', buffering: int = -1, encoding: Optional[str] = None, errors: Optional[str] = None, newline: Optional[str] = None, closefd: bool = True, opener: Optional[Callable[[str, int], int]] = None)
    """
    def __init__(self, name: str, mode: str = 'r', buffering: int = -1, encoding: Optional[str] = None, errors: Optional[str] = None, newline: Optional[str] = None, closefd: bool = True, opener: Optional[Callable[[str, int], int]] = None):
        pass
    
    
    def __repr__(self) -> str:
        """
        Return repr(self).
        """
        pass
    
    
    def close(self) -> None:
        """
        Flush and close this file.
        
        This method has no effect if the file is already closed.
        """
        pass
    
    
    def fileno(self) ->
