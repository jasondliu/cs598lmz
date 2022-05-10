import io
class File(io.RawIOBase):
    pass
    
class FileIO(io.FileIO):
    pass

class FileText(io.TextIOWrapper):
    pass


class PyFileObject(RawIOBase):
    """A file object that should be compatiple with the C PyFileObject
    """
    def __init__(self, file = "/dev/tty", mode="r", bufsize=-1):
        """Open a file
        """
        if not isinstance(file, str):
            raise TypeError("Open does not accept non-strings")
        self.file = open(file, mode=mode, buffering=bufsize)
        
    def close(self, state=None):
        """Close a file.
        """
        self.file.close()
        
    def fileno(self):
        """Get a fileno.
        """
        return self.file.fileno()
    
    def flush(self):
        """Flush a file.
        """
        self.file.flush()
        
    def isatty(self):
        """Return whether a file is a t
