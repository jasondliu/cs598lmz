import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

class Bytes:
    def __init__(self, data, errors="strict"):
        self.data = data
        self.offset = 0
        self.errors = errors

    def read(self, size):
        end = self.offset + size
        res = self.data[self.offset:end]
        self.offset = end
        return res

    def read1(self):
        res = self.data[self.offset:self.offset+1]
        self.offset += 1
        if not res:
            raise EOFError
        return res

    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = len(self.data) + offset
        else:
            assert 0, "whence must be 0, 1, or 2"

    def tell(self):
        return self.offset

    def close(self):
        pass

    def __iter__(self):
       
