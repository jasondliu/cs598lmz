from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# You can do the same thing with zlib
# import zlib
# zlib.decompress(compressed_data)

# You can also use the 'with' keyword to automatically close the file after 
# the nested block of code. The file is closed as soon as Python leaves the 
# with block, even if exceptions occur within it.
with open('somefile.txt', 'rt') as f:
    data = f.read()

# The file object returned by open is also an iterator that produces the lines 
# of the file.
with open('somefile.txt', 'rt') as f:
    for line in f:
        print(line)

# If you want to write data to a file, use the 'wt' mode instead.
with open('somefile.txt', 'wt') as f:
    f.write(text2write)

# If you want to append instead of write, use the 'at' mode.
with open('somefile.txt', 'at') as f:
    f.write(text2write)
