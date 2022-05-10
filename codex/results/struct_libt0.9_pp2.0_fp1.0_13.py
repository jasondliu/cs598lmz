import _struct
import zlib

class ZipFm(object):
    def __init__(self, fm, mode='r'):
        object.__setattr__(self, 'fm', fm)
        object.__setattr__(self, 'mode', mode)
        object.__setattr__(self, '_fp', None)
        object.__setattr__(self, '_crc32', 0)
    
    @property
    def _fp(self):
        return object.__getattribute__(self, '_fp')

    def __getattr__(self, name):
        return getattr(object.__getattribute__(self, 'fm'), name)

    def __setattr__(self, name, value):
        return setattr(object.__getattribute__(self, 'fm'), name, value)

    def __enter__(self):
        return self

    def __exit__(self, *err):
        return self.close()
    
    def read(self, size=-1):
        if self.mode == 'r':
            if
