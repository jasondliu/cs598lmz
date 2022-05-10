import bz2
# Test BZ2Decompressor
with bz2.BZ2File('example.bz2','r') as bz2_file:
    decompressor = bz2.BZ2Decompressor()
    with open('new_file.txt', 'wb') as fp:
        for block in iter(lambda : bz2_file.read(1024 * 100), b''):
            fp.write(decompressor.decompress(block))
print(open('new_file.txt').read(100))

# BZ2File
# Open a bzip2-compressed file in binary or text mode.

# The mode can be 'r' 
# or 'rb' for reading (default), 
# 'w' or 'wb' for writing, 
# and 'a' or 'ab' for appending. 

# The file will be created if it doesn’t exist when opened for writing or appending; it will be truncated when opened for writing. Add a '+' to the mode to allow simultaneous reading and writing.
 
# When opened for writing, the file will be created if it doesn
