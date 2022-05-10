import io
class File(io.RawIOBase):
    """
    Simulate a file object.
    """
    def __init__(self, filename):
        self.filename = filename

    def close(self):
        return

    def read(self, size=-1):
        with open(self.filename, "rb") as f:
            data = f.read()
        return data

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        return

    def tell(self):
        return 0

class Image(object):
    """
    Represent an image.

    Attributes:
        - `data`: a bytes object containing the image data.
        - `size`: image size as a tuple of width and height.
        - `mode`: image mode.
    """
    def __init__(self, data, size, mode):
        self.data = data
        self.size = size
        self.mode = mode

def open(fp):
    """
    Open an image file.

    The `fp` argument can
