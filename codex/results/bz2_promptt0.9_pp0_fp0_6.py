import bz2
# Test BZ2Decompressor
data = open('test.bz2', 'rb').read()
decompressor = bz2.BZ2Decompressor() # Create a compressor object
decompressor.decompress(data)  # Decompress data

# For decompressing strings, try:
data = open('test.bz2', 'rb').read()
decompressor = bz2.BZ2Decompressor()
uncompressed_data = decompressor.decompress(data)

# To decompress file-like objects, which support the same methods as ordinary files, use:
# datafile = open('test.bz2', 'rb')
# decompressor = bz2.BZ2Decompressor()
# for data in iter(lambda : datafile.read(100 * 1024), b''):
#     uncompressed_data = decompressor.decompress(data)

# bz2.BZ2File
# - similary to gzip.GzipFile and zipfile.ZipFile objects.
# - can perform fully transparent decompression or incremental decompression of specifically compressed files.


