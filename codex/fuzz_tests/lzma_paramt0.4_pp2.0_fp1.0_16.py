from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# b'hello world\n'

# The LZMA library also supports a stream interface for compressing and decompressing data.
# The LZMAFile class in the lzma module is a file-like object that reads and writes LZMA-compressed data.
# The following example shows how to compress some data and write it to a file:

import lzma
with lzma.open('lorem.xz', 'w') as f:
    f.write(b'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ac nibh.')

# The file is written in the xz format, which is the default format used by the LZMA library.
# The format can be changed by specifying the format keyword argument.
# The following example shows how to read the compressed data back:

with lzma.open('lorem.xz') as f:
    file_content = f.read()

# The LZMA library also supports the bz2 format.
# The following example shows how to
