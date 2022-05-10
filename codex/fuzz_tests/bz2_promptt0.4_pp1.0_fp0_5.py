import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
input_file = open('/Users/kolbt/Desktop/compressed_dump.tar.bz2', 'rb')
output_file = open('/Users/kolbt/Desktop/uncompressed_dump.tar', 'wb')

while True:
    block = input_file.read(1024)
    if not block:
        break
    output_file.write(d.decompress(block))

input_file.close()
output_file.close()
# Test BZ2Compressor
c = bz2.BZ2Compressor()
input_file = open('/Users/kolbt/Desktop/uncompressed_dump.tar', 'rb')
output_file = open('/Users/kolbt/Desktop/compressed_dump.tar.bz2', 'wb')

while True:
    block = input_file.read(1024)
    if not block:
        break
    output_file.write(c.compress(block))

output_file.write(c
