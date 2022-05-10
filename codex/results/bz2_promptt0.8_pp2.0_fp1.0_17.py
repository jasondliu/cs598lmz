import bz2
# Test BZ2Decompressor.read1() with one-byte-at-a-time decompression
#
# read1() is optimized for use in a loop where you continuously call read1() in
# each iteration and repeatedly pass the partially decompressed result to
# another layer until the entire data stream has been decompressed.
#
# The optimized loop avoids creating a new string object in each iteration by
# re-using the same bytes object and changing only its length.
#
# Without read1(), the code would look like this:
#
# output = b''
# while True:
#     fragment = d.decompress(b'\x00' * 32 * 1024)
#     if not fragment:
#         break
#     output += fragment

d = bz2.BZ2Decompressor()
data = ''
while True:
    fragment = d.decompress(b'\x00' * 32 * 1024)
    if not fragment:
        break
    data += fragment
assert data == 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\
