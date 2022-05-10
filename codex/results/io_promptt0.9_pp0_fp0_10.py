import io
# Test io.RawIOBase
class C(io.RawIOBase):
    def readable(self):
        return True

    def seekable(self):
        return True

    def writable(self):
        return False

C.readinto.im_func, object.readinto.im_func
C.seek.im_func, object.seek.im_func
C.tell.im_func, object.tell.im_func
C.readall.__get__(C()), io.RawIOBase.readall.__get__(C())
C.read.__get__(C()), io.RawIOBase.read.__get__(C())
C.read1.__get__(C()), io.RawIOBase.read1.__get__(C())
C.write.__get__(C())
C.flush.__get__(C())
#TODO io.BufferedIOBase, io.BufferedReader, io.BufferedWriter, io.BufferedRWPair,
#TODO io.BytesIO, io.StringIO, io.TextIOBase, io.
