import lzma
# Test LZMADecompressor.decompress()

# open a compressed file, decompress it and save as decompressed.txt
with lzma.open('./compressed', mode='rb') as infile:
    with open('./decompressed.txt', 'wb') as outfile:
        decompressor = lzma.LZMADecompressor()
        while True:
            decompressed = decompressor.decompress(infile.read(1024))
            if decompressed:
                outfile.write(decompressed)
            else:
                break
 
# open a LZMA stream and decompress it
with open('./compressed', mode='rb') as infile:
    with lzma.open('./decompressed_stream.txt', mode='wb') as outfile:
        decompressor = lzma.LZMADecompressor()
        for line in infile:
            outfile.write(decompressor.decompress(line))
        outfile.write(decompressor.flush())
 
# open a LZMA stream and decompress it
