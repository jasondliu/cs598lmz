from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# more efficient compression
compressor = BZ2Compressor()
for block in generate_blocks():
    compressed = compressor.compompress(block)
    send_to_remote(compressed)
remaining = compressor.flush()
send_to_remote(remaining)

# BZ2File class to use the bz2 module's file-like classes
BZ2File('data.bz2').read(100)

# tempfile module to create temporary files
import os
from tempfile import TemporaryFile, NamedTemporaryFile

# TemporaryFile - create a temporary file in the platforms default
# temporary directory that is automatically deleted after the file is closed

# NamedTemporaryFile - create a temporary file with a unique name in the
# platform's default temporary directory
tmp = NamedTemporaryFile(prefix='myapp_')
print tmp.name
tmp.close()

# tempnam function - create a unique temporary file name
tempname = tempnam()
print tempname

# mkstemp function - create a temporary file and return a file descriptor
filename
