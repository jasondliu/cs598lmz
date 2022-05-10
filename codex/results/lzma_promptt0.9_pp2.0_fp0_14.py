import lzma
# Test LZMADecompressor

class Myfile(object):
    def __init__(self, filename):
        self.filename = filename

    def read(self, bytes=None):
        # See the docs of lzma.open() for why func should return bytes
        with open(self.filename, 'rb') as fp:
            s = fp.read()
        return s

filename = sys.argv[1]
x = Myfile(filename)
d = lzma.LZMADecompressor()

loop = 300

start_time = time.time()
for i in range(loop):
    x.read()
e = time.time() - start_time
print("open() takes {:.2f} us".format(e / loop * 1e6))

start_time = time.time()
for i in range(loop):
    d.decompress(x.read())
e = time.time() - start_time
print("lzma.py takes {:.2f} us".format(e / loop * 1e6))

start_time = time
