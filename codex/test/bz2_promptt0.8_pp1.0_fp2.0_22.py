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

