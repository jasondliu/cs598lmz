import io
class File(io.RawIOBase):
    """ 
        File object wrapper. Defines open, read, readline and seek functions
        for file
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_handle = open(file_path, "rb")#open file

    def open(self):
        self.file_handle = open(self.file_path, "rb")

    def read(self, size=-1):
        """Return bytes from the file_handle"""
        assert self.file_handle is not None, "File handle is None."
        return self.file_handle.read(size)

    def readline(self, size=-1):
        """Return bytes from the file_handle"""
        assert self.file_handle is not None, "File handle is None."
        return self.file_handle.readline(size)

    def seek(self, offset, whence=0):
        seek_flag = "".join([whence.upper(), "SEEK"])

        if seek_flag not in ["RSEEK" , "WSEE
