import bz2
# Test BZ2Decompressor
bz_decompressor = BZ2Decompressor()
bz_decompressor.decompress(bz2_compressed_data)

# Test BZ2File
with BZ2File('compressed_data.bz2', 'wb') as f:
    f.write(bz2_compressed_data)

with BZ2File('compressed_data.bz2', 'r') as f:
    print(f.read())

# Cleanup
os.remove('compressed_data.bz2')

# BZ2File does not have a decompress() method
# BZ2File is a context manager and returns a file-like object
# BZ2File has a .read() method, but no .write() method
# but only works on files

import bz2

with open('myfile.txt', 'rt') as input:
    with bz2.open('myfile.txt.bz2', 'wt') as output:
        for line in input:
            output.write(line)
# bz2.
