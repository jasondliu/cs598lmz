import io
class File(io.RawIOBase):
    def read(self, n=-1):
        print("reading...")
        return "imagine this came from a file"
    
    def seekable(self):
        print("file is seekable")
        return False

f = File()
f.read(32)

f.seekable()

print(f.readable())

class ReadStream(io.RawIOBase):

    def read(self, n=-1):
        return "imagine this came from a socket"
    
    def readable(self):
        return True

file = File()

stream = ReadStream()

reader = io.BufferedReader(stream)

with io.open("some_file.txt") as rf:
    closed = rf.closed
    close = rf.close()
    fc = rf.flush()
    name = rf.name
    mode = rf.mode
    bufsz = rf.buffer_size
    print(rf.newlines)
    content = rf.read()
    contnets = rf.read(31)
