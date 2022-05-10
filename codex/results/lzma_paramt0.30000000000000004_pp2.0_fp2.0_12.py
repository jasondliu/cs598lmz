from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# b'Hello World!\n'

# LZMAFile is a file-like object that wraps a LZMA stream. It can be used to
# decompress data that was compressed using the lzma module.

# LZMAFile can be used in a with statement. The stream is closed when the
# with block is exited.

from lzma import LZMAFile
with LZMAFile(lzma_file) as lz:
    print(lz.read())

# b'Hello World!\n'

# LZMAFile can also be used as a context manager without a with statement.
# In this case, the caller is responsible for closing the file.

lz = LZMAFile(lzma_file)
try:
    print(lz.read())
finally:
    lz.close()

# b'Hello World!\n'

# LZMAFile can be used to decompress data that was compressed using the lzma
# module.

lzma_
