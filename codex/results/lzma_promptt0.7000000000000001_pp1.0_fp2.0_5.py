import lzma
# Test LZMADecompressor
lz = lzma.LZMADecompressor()
decompressed_data = lz.decompress(compressed_data)
# Data is identical to the uncompressed file
decompressed_data == original_data

# Compress a file with XZ
with open('somefile', 'rb') as input:
    with lzma.open('somefile.xz', 'w') as output:
        output.write(input.read())

# Decompress a file with XZ
with lzma.open('somefile.xz') as f:
    file_content = f.read()

# Compress with LZMA
with open('newfile', 'w') as output:
    with lzma.open('somefile.xz') as input:
        output.write(input.read())

import bz2

# Compress a file with BZ2
with open('somefile', 'rb') as input:
    with bz2.open('somefile.bz2', 'wb') as output:
        output.writelines(
