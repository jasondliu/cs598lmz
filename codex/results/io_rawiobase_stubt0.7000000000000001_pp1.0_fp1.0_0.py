import io
class File(io.RawIOBase):
    def read(self, n=-1):
        pass
    def readable(self):
        return True
    def seekable(self):
        return True
    def writable(self):
        return False
    def writelines(self, lines):
        pass
    def seek(self, offset, whence=0):
        pass

class Blob(object):
    def __init__(self, name, contentType=None, contentEncoding=None,
                 dispositionType=None, dispositionParams=None,
                 defaultType=None, defaultParams=None, **params):
        self.name = name
        self.contentType = contentType
        self.contentEncoding = contentEncoding
        self.dispositionType = dispositionType
        self.dispositionParams = dispositionParams
        self.defaultType = defaultType
        self.defaultParams = defaultParams
        self.params = params
    def __repr__(self):
        return '<%s %r>' % (
            self.__class__.__name__,
            self.name
        )
