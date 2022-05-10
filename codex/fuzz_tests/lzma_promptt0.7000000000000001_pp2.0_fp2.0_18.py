import lzma
# Test LZMADecompressor with non-seekable input
# and a .read() method that returns shorter data.
class NonSeekableInput:
    def __init__(self, data):
        self.data = data
        self.pos = 0
    def read(self, size):
        chunk = self.data[self.pos:self.pos+size]
        return chunk
class NonSeekableInput2(NonSeekableInput):
    def read(self, size):
        chunk = self.data[self.pos:self.pos+size]
        self.pos += len(chunk)
        return chunk
class NonSeekableInput3(NonSeekableInput):
    def read(self, size):
        chunk = self.data[self.pos:self.pos+size]
        self.pos += len(chunk) // 2
        return chunk
comp = lzma.LZMACompressor()
compressed = comp.compress(b"x" * 100) + comp.flush()

# Test the .read() method that returns shorter data
fd = NonSeekableInput(comp
