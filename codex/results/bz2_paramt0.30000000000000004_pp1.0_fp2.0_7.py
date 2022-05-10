from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# This is the data from the previous exercise
bz_file = open('example.bz2', 'rb')
data = bz_file.read()
bz_file.close()

# TODO: decompress data here
decompressed_data = BZ2Decompressor().decompress(data)

# TODO: write the uncompressed data to a file
uncompressed_file = open('uncompressed.txt', 'wb')
uncompressed_file.write(decompressed_data)
uncompressed_file.close()

# TODO: open the uncompressed file and print the first 3 lines
uncompressed_file = open('uncompressed.txt', 'rb')
for i
