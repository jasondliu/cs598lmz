import io
class File(io.RawIOBase):
    """ Represents a file on the server, files created onboard are treated as a 
    temporary file which will be deleted in 60 seconds unless uploaded.
    """

    def __init__(self):
        self.data = None # Base64 encoded data

    def read(self):
        if self.data is None:
            return None
        else:
            return self.data
