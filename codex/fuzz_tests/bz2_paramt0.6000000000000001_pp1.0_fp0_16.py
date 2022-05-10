from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(bytes(test_string, 'utf-8')), max_length=len(test_string) * 8)

"""

"""
import zlib
zlib.compress(bytes(test_string, 'utf-8'))

"""

"""
import zlib
zlib.decompress(zlib.compress(bytes(test_string, 'utf-8')))
"""

"""
import lzma
lzma.compress(bytes(test_string, 'utf-8'))
"""

"""
import lzma
lzma.decompress(lzma.compress(bytes(test_string, 'utf-8')))
"""

"""
import lz4
lz4.compress(bytes(test_string, 'utf-8'))
"""

"""
import lz4
lz4.decompress(lz4.compress(bytes(test_string, 'utf-8')))
"""

"""
import lzma
import bz2
import z
