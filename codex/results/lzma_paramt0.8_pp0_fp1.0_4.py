from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_ALONE, filters=None).decompress(data)

##################################################
# Compress a file-like object.

from lzma import open
with open('file.xz', 'rb') as input, \
     open('file.lzma', 'wb') as output:
    decompressor = LZMADecompressor()
    for block in iter(lambda: input.read(1024 * 1024), b''):
        output.write(decompressor.decompress(block))
    output.write(decompressor.flush())

##################################################
# Encoding

from lzma import open
with open('file.xz', 'rt', encoding='utf-8') as input, \
     open('file.lzma', 'wt', encoding='utf-16') as output:
    decompressor = LZMADecompressor()
    for block in iter(lambda: input.read(1024 * 1024), b''):
        output.write(decompressor.decompress(block).decode('utf-8'))
    output
