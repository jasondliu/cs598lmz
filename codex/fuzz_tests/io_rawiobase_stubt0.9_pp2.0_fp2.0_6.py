import io
class File(io.RawIOBase):
    """file(name: string[, mode: string]) -> file object
    Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
    writing or appending.  The file will be created if it doesn't exist
    when opened for writing or appending; it will be truncated when
    opened for writing.  Add a 'b' to the mode for binary files.
    Add a '+' to the mode to allow simultaneous reading and writing.
    If the file cannot be opened, IOError is raised.
    close() is called automatically when the file is deleted.
    """
    def __init__(self, filename, mode="r"): self.file = open(filename, mode)
    def close(self):
        WriteFile(self.file.name)
        self.file.close()
    def readable(self): return self.file.readable()
    def read(self, size=-1): return self.file.read(size)
    def readinto(self, b): return self.file.readinto(b)
    def readline(self
