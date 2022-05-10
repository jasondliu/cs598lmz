import lzma
lzma.decompress(compressed_data)

# The result will be a bytes object.
# To get a string, use the decode() method.

# This example is a little bit contrived, since you're
# unlikely to compress a string and then immediately
# decompress it. Still, it's a common operation.

# To compress a file, use the compressfile() function:

with open('somefile.csv', 'rb') as input:
    with lzma.open('somefile.csv.xz', 'w') as output:
        output.write(input.read())

# This writes the compressed data to the file somefile.csv.xz.
# To decompress, use lzma.open() in read mode to read the data
# into a file-like object and then write() the decompressed data
# to another file.

# The LZMAFile class is used in a way similar to how gzip.GzipFile()
# and bz2.BZ2File() are used. For example:

with lzma.open('somefile.csv.
