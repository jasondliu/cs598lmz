import bz2
# Test BZ2Decompressor with multiple streams
buf = []
def read_from(source):
    d = BZ2Decompressor()
    try:
        while True:
            buf.append(d.decompress(source.read(1024)))
    except EOFError:
        return b''.join(buf)

try:
    read_from(bz2.BZ2File('bz2_file.py', 'rb'))
except EOFError:
    pass

# Test BZ2Compressor with multiple streams
buf = []
def write_to(sink):
    c = BZ2Compressor(9)
    while True:
        chunk = sink.read(1024)
        if not chunk:
            break
        buf.append(c.compress(chunk))
    buf.append(c.flush())

write_to(open('bz2_file.py', 'rb'))
open('bz2_file.bz2', 'wb').write(b''.join(buf))

# Test BZ2File
f = open('bz2_file
