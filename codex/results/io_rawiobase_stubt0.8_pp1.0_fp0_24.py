import io
class File(io.RawIOBase):
    def read(self, n=-1):
        pass
    def fileno(self):
        pass
    def write(self, b):
        pass
    def readinto(self, b):
        pass
    def seek(self, offset, whence=0):
        pass
    def readline(self, length=None):
        pass
    def truncate(self, size=None):
        pass
    def readable(self):
        pass
    def writable(self):
        pass
    def seekable(self):
        pass

def open(file, mode='r', buffering=-1, encoding=None,
         errors=None, newline=None, closefd=True, opener=None):
    return File()

def _prepend_doc(what, doc):
    """Prepend a docstring to an object's __doc__.

    What can be either a class or a function, and its __doc__
    attribute will be modified in place. The docstring will be
    prepended to the original docstring if it exists, or will
    replace it otherwise.
   
