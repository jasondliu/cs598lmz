import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes'.format(len(data)))

decompressor = bz2.BZ2Decompressor()
try:
    # Multiple calls to decompress() can be made to process a stream of data in chunks
    # (e.g. from a file), compared to decompress() which expects a single chunk.
    # If the data is incomplete, decompress() will raise an EOFError exception.
    # The decompress() method will return the uncompressed data, or an empty bytes object if EOF was reached.
    print(decompressor.decompress(data))
    print(decompressor.decompress(data))
    print(decompressor.decompress(data))
    print('Output is {}
