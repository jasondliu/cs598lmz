from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO, memlimit=None, filters=None)
</code>
How can i compress and decompress stream of data with LZMA in python 3.x?


A:

<code>#!/usr/bin/python3
# -*- coding: utf-8 -*-

# compress
import lzma
data = b"lotsofdata"
with lzma.open("data.xz", "wb") as f:
    f.write(data)

# decompress
with lzma.open("data.xz") as f:
    file_content = f.read()
</code>

