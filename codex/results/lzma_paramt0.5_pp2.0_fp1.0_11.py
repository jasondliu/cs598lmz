from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# b'Hello World!Hello World!Hello World!Hello World!'

# It is also possible to decompress a stream of data.

from io import BytesIO

compressor = LZMACompressor()

buf = BytesIO()
buf.write(compressor.compress(b'Hello World!Hello World!'))
buf.write(compressor.compress(b'Hello World!Hello World!'))
buf.write(compressor.compress(b'Hello World!Hello World!'))
buf.write(compressor.flush())

buf.seek(0)
decompressor = LZMADecompressor()
decompressed_data = b''
while True:
    chunk = buf.read(1024)
    if not chunk:
        break
    decompressed_data += decompressor.decompress(chunk)

decompressed_data
# b'Hello World!Hello World!Hello World!Hello World!'

# The LZMAFile class implements an easy-to-use interface to .xz files.

import
