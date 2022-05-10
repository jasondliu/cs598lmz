import lzma
# Test LZMADecompressor
# This is used in production
#
# Author: Stefan Hegglin
# Date:   2018-11-29
#
# Description:
# This script is used to test the LZMADecompressor class

# buffer size
BUFFER_SIZE = 1024

# open the file to decompress
infile = open('../testdata/lzma/test_compressed.lzma', 'rb')
# read the header
header = infile.read(13)
# create our decompressor
decomp = lzma.LZMADecompressor()
# open the output file
outfile = open('../testdata/lzma/test_decompressed.lzma', 'wb')
# decompress the file and write it to the output file
# one buffer at a time
while True:
    data = infile.read(BUFFER_SIZE)
    if not data:
        break
    outfile.write(decomp.decompress(data))

# close the files
infile.close()
outfile.close()
