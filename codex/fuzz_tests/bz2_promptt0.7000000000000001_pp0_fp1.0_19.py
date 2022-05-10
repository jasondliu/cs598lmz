import bz2
# Test BZ2Decompressor
# https://docs.python.org/3/library/bz2.html
# https://stackoverflow.com/questions/16969103/bz2-decompress-a-file-in-python
decompress = bz2.BZ2Decompressor()

f = decompress.decompress(open(filename, 'rb').read())

# Print the decompressed data
# print('Decompressed is {} bytes'.format(len(f)))
# print(f)

# Read the test file on the fly
# Not all of the file is read.
# Only the first line of text is read.
# The rest of the data is discarded
#print(f.readline())


# Read the test file on the fly
# Not all of the file is read.
# Only the first line of text is read.
# The rest of the data is discarded

# Test BZ2File
# https://docs.python.org/3/library/bz2.html
# https://stackoverflow.com/questions/16969103/bz2-dec
