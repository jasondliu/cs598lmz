import lzma
# Test LZMADecompressor
fd_lzma = lzma.LZMADecompressor()
# Get the next bunch of data to decompress
compressed = file_obj.read(1024)
# Decompress it
uncompressed = fd_lzma.decompress(compressed)
# This function returns a bytearray for python3 or bytes for python2
uncompressed.decode()


# get length of file:
file_obj.seek(0, os.SEEK_END)
file_size = file_obj.tell()

# seek to the beginning
file_obj.seek(0)
# iterate through by chunks
buffer_size = 100000
uncompressed = bytearray()
while file_obj.tell() < file_size:
    compressed = file_obj.read(buffer_size)
    uncompressed = fd_lzma.decompress(compressed)
    # add to your memory
    rr = uncompressed.decode('utf-8')
    print(type(rr))
    print(rr)
