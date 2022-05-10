import lzma
# Test LZMADecompressor, streaming data
import io

comp = lzma.LZMACompressor(format=lzma.FORMAT_ALONE)
data = comp.compress(b'hello, world\n')
data += comp.flush()

decomp = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
with io.BytesIO(data) as f:
    while True:
        block = f.read(5)
        if not block:
            break

        print(repr(decomp.decompress(block)))

print(decomp.eof)
print(decomp.unused_data)
