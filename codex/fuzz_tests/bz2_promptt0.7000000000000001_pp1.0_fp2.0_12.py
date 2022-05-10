import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

# decompressed_data = decompressor.decompress(compressed_data)

# print('Decompressed is {} bytes'.format(len(decompressed_data)))
# print(decompressed_data)
for line in open('enwiki-latest-pages-articles.xml.bz2'):
    line = line.strip()
    if line:
        decompressed_data = decompressor.decompress(line)
        print('Decompressed is {} bytes'.format(len(decompressed_data)))
        print(decompressed_data)

print(decompressor.eof)

decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
print(dec
