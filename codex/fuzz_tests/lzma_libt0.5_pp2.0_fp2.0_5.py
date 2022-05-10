import lzma
lzma.open
lzma.open(path, mode='rb')

from lzma import LZMAFile
with LZMAFile(path, mode='wb') as f:
    f.write(b'hello world')
with LZMAFile(path, mode='rb') as f:
    print(f.read())

lzma.LZMAFile
lzma.LZMAFile(filename, mode='rb', format=None, check=-1, preset=None, filters=None)

lzma.open
lzma.open(filename, mode='rb', format=None, check=-1, preset=None, filters=None)

from lzma import LZMACompressor, LZMADecompressor
compressor = LZMACompressor()
compressor.compress(b'hello world')
compressor.flush()

decompressor = LZMADecompressor()
decompressor.decompress(compressor.compress(b'hello world'))
decompressor.decompress(compressor.flush())


