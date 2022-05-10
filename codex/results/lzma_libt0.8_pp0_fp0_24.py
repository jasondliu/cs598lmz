import lzma
lzma.__doc__ = """
This module provides a class and convenience functions for
compressing and decompressing data with the LZMA algorithm.
"""

import lzma
from io import BytesIO

data = b'Four score and seven years ago...'

with BytesIO() as buf:
    with lzma.open(buf, 'w') as f:
        f.write(data)

    compressed_data = buf.getvalue()

with BytesIO(compressed_data) as buf:
    with lzma.open(buf) as f:
        restored = f.read()

assert data == restored

import lzma
from io import BytesIO

data = b'Four score and seven years ago...'

with BytesIO() as buf:
    with lzma.open(buf, 'w', preset=9) as f:
        f.write(data)

    compressed_data = buf.getvalue()

print(len(compressed_data), len(data))

# C:\App\python36\Lib\site-
