import _struct

from _io import DEFAULT_BUFFER_SIZE
_check_byteslike = _struct.check_byteslike

def _get_memory(data):
    if isinstance(data, memoryview):
        return data.obj
    return data

class BytesIO(_BufferedIOBase):
    def __init__(self, initial_bytes=None):
        self._buffer = bytearray()
        self._pos = 0
        if initial_bytes is not None:
            self.write(initial_bytes)
    def __getstate__(self):
        if self.closed:
            raise ValueError('__getstate__ on closed file')
        return self.__dict__.copy()
    def __setstate__(self, state):
        self.__dict__.update(state)
    def getbuffer(self):
        if self.closed:
            raise ValueError('getbuffer on closed file')
        return memoryview(self._buffer)
    def getvalue(self):
        if self.closed:
            raise ValueError('getvalue on closed file')
       
