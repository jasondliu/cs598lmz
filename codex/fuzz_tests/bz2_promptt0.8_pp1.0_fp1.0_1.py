import bz2
# Test BZ2Decompressor

with open('c:/Users/matt.matuk/Downloads/gwik.txt', 'r') as file_handle:
    with bz2.BZ2Decompressor() as decompressor:
        for block in iter(lambda: file_handle.read(100 * 1024), b''):
            print(decompressor.decompress(block))

# Test BZ2Compressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
with open('c:/Users/matt.matuk/Downloads/gwik.txt', 'wb') as file_handle:
    with bz2.BZ2Compressor() as compressor:
        for block in [data[0:10], data[10:20], data[20:30], data[30:40], data
