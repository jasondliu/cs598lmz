import io
class File(io.RawIOBase):

    def __init__(self, c_file: ctypes.c_void_p, close_c_file: bool = True):
        self.close_c_file = close_c_file
        self.c_file = c_file

    def readable(self):
        return True

    def seekable(self):
        return False

    def __getattr__(self, item):
        try:
            return getattr(lib, item)
        except AttributeError:
            return getattr(self.c_file.contents, item)

    def close(self):
        if self.close_c_file:
            self.close_c_file = False
            return lib.wasm_byte_vec_delete(self.c_file)
        return 0

    def pend(self, b, n):
        self._checkClosed()
        exec = True
        while exec:
            p = lib.wasm_byte_vec_append_bytes(self.c_file, bytearray(b[:n]))
            if p == 0:
               
