import lzma
# Test LZMADecompressor.decompress()
for msg in ['', 'a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa']:
    buf = io.BytesIO()
    with lzma.LZMADecompressor() as dec:
        buf.write(dec.decompress(lzma.compress(msg)))
        buf.seek(0)
        print(buf.read())

# Test LZMADecompressor to work on streams
import sys
if sys.version_info < (3,):
    unichr = unichr
    int2byte = chr
    range_type = xrange
else:
    unichr = chr
    int2byte = lambda i: bytes((i,))
    range_type = range

def stream_decompress(infile, outfile):
    dec = lzma.LZMADecompressor()
    while True:
        chunk = infile.read(1024)
        if not chunk:
            break
        outfile.write(dec.
