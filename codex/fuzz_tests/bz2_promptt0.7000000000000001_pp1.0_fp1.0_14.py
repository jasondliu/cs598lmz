import bz2
# Test BZ2Decompressor Class
decompressor = bz2.BZ2Decompressor()
data = decompressor.decompress(bz2_data)
data == original_data

# Use the decompress() method to decompress the entire BZ2 file
file = bz2.BZ2File('example.bz2')
data = file.read()

# BZ2File class automatically decompresses the data
file = bz2.BZ2File('example.bz2', 'rb')
file.read(100)
file.tell()
file.seek(0)
file.read(50)
file.seek(-10, 2)
file.read()

# The compressed data is not written until you close the file
file.write(b'This is the added data.')
file.close()

# You can open a file in online mode to read and write compressed data on the fly
file = bz2.BZ2File('example.bz2', 'wb')
file.write(b'This is the added data.')
file.close()

# The compressed data is
