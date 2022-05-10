import io
class File(io.RawIOBase):
    """File(name: str, mode: str='r', buffering: int=0, encoding: Optional[str]=None,
        errors: Optional[str]=None, newline: Optional[Union[bytes, str, None]]=None,
        closefd: bool=True, opener: Optional[Callable[..., int]]=None)
        Create a file object with the os default encoding. Line buffering is
        enabled if mode is 'r' (unless buffering is explicitly set to 0 or
        a negative value). The file is not buffered, so an extra read() call
        may be needed to see the last write() output.
    """
    @classmethod
    def open(cls, name, mode='r', buffering=-1, encoding=None,
        errors=None, newline=None, closefd=True, opener=None, **kwargs):
        """open(name: str, mode: str='r', buffering: int=0, encoding: Optional[str]=None,
            errors: Optional[str]=None, newline: Optional[Union[bytes, str, None]]=None
