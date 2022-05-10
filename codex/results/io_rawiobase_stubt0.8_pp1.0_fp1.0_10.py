import io
class File(io.RawIOBase):
    def __init__(self, sio):
        # copy the StringIO from the caller
        self.__sio = StringIO(sio.getvalue())
        # set the position to 0
        self.__sio.seek(0)
    def read(self, l=-1):
        return self.__sio.read(l)
    def readable(self):
        return True
    def seekable(self):
        return True
    def seek(self, l, mode=0):
        return self.__sio.seek(l,mode)

if __name__ == "__main__":
    sio = StringIO()
    sio.write(bytes(u"hello", "utf-8"))
    with ZipFile(File(sio), "w") as zf:
        zf.writestr("foo.txt", "bar")
</code>

