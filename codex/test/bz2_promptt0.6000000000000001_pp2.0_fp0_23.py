import bz2
# Test BZ2Decompressor
# decompressor = bz2.BZ2Decompressor()
#
# with open('test.bz2', 'rb') as input:
#     with open('test.out', 'wb') as output:
#         while True:
#             block = input.read(1024)
#             if not block:
#                 break
#             output.write(decompressor.decompress(block))
#
# print('Decompressed.')

# Test BZ2Compressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(data)
print(compressed_data)

compressor.flush()
