import io
class File(io.RawIOBase):
    def write(self, string):
        pass
    def tell(self):
        pass
    def seek(self, offset, whence=0):
        pass
    def truncate(self, size=None):
        pass
    def isatty(self):
        pass
    def flush(self):
        pass
    def fileno(self):
        pass
    def close(self):
        pass
    def readable(self):
        pass
    def writable(self):
        pass
    def seekable(self):
        pass
# files are not readable
File().readable()
# files are writable
File().writable()
# files are seekable
File().seekable()
 
# files are not isatty()
File().isatty()
 
# files are not isatty()
File().isatty()
 
# files have a fileno()
File().fileno()
 
# files have a write()
File().write('abc')
 
# files have a writelines()
File().writelines(['a', 'b', 'c'
