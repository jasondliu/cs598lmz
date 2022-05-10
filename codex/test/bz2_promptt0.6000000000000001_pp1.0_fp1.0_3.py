import bz2
# Test BZ2Decompressor by piping data through it.
# Feed bytes into the decompressor object, and print the result.
# The bz2 module includes a function for decompressing a whole file at once.
# This function will decompress a file-like object, which we can simulate by
# writing our compressed data to a BytesIO object and then reading from it.
# The bz2.decompress() function expects bytes-like objects, so we must
# encode the string before writing it.

compressed_data = bz2.compress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
print('Compressed is {} bytes'.format(len(compressed_data)))
print(compressed_data)

decompressor = bz2.BZ2Decompressor()
