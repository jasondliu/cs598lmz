import lzma
# Test LZMADecompressor
with open("../data/sample_xz.xz", "rb") as f:
    decompressor = lzma.LZMADecompressor()
    with open("../data/sample_xz.txt", "wb") as out:
        for buf in iter(lambda: f.read(1024), b''):
            out.write(decompressor.decompress(buf))
        out.write(decompressor.flush())
 
# Test LZMACompressor
with open("../data/sample.txt", "rb") as f:
    compressor = lzma.LZMACompressor()
    with open("../data/sample_xz.xz", "wb") as out:
        for buf in iter(lambda: f.read(1024), b''):
            out.write(compressor.compress(buf))
        out.write(compressor.flush())

# Pattern Matching
import re
match = re.search(r'ii', 'piiig')
match.group()
match = re.search(r'\d\d\d
