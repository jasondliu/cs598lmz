from bz2 import BZ2Decompressor
BZ2Decompressor

# uncompresses the data
decompressor = BZ2Decompressor()
data = decompressor.decompress(compressed_data)
print(len(data))

# outputs the data, which is the same as the original
print(data)

# BZIP2 compression: http://www.bzip.org/
# compression algorithm: https://xlinux.nist.gov/dads/HTML/bzip2Compress.html
# decompression algorithm: https://xlinux.nist.gov/dads/HTML/bzip2Decompress.html
