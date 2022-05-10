import bz2
# Test BZ2Decompressor
decompressor_bz2 = bz2.BZ2Decompressor()
file_bz2 = bz2.BZ2File('data/audio.bz2')
output_temp = open('data/audio.wav', 'wb')
while True:
    block = file_bz2.read(1024)
    if not block:
        break
    decompressed = decompressor_bz2.decompress(block)
    if decompressed:
        output_temp.write(decompressed)
output_temp.close()
# Test LZMADecompressor
decompressor_lzma = lzma.LZMADecompressor()
file_lzma = lzma.open('data/audio.lzma')
output_temp = open('data/audio.wav', 'wb')
while True:
    block = file_lzma.read(1024)
    if not block:
        break
    decompressed = decompressor_lzma.decompress(block)
    if decompressed:
        output_temp.write
