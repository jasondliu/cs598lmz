import bz2
# Test BZ2Decompressor
with open('wiki.xml.bz2', 'rb') as fp:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: fp.read(100*1024), b''):
        # print(block)
        print(block[0:100])
        out = decompressor.decompress(block)
        print(out[0:100])
        # print(out)

# bz2.decompress(block)
import re
pattern = re.compile(r"<title>(.*)</title>")
with open('wiki.xml.bz2', 'rb') as fp:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: fp.read(100*1024), b''):
        out = decompressor.decompress(block)
        print(pattern.findall(out.decode('utf-8')))

with open('wiki.xml.bz2', 'rb') as fp:
    decompressor = bz2.BZ
