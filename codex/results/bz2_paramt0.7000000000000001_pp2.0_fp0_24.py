from bz2 import BZ2Decompressor
BZ2Decompressor()

# decompress the data
fileobj = BZ2File('example.bz2')
data = fileobj.read()

# write the decompressed data to a file
newfileobj = open('uncompressed.txt', 'wb')
newfileobj.write(data)
newfileobj.close()

'''
BZ2File is a class that acts like a file object but uses BZ2Decompressor to
decompress data on the fly to a file. BZ2File takes the same parameters as
open() to open the underlying file object.
'''
