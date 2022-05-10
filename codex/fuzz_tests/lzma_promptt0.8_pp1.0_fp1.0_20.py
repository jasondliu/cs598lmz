import lzma
# Test LZMADecompressor
# lzd = lzma.LZMADecompressor()
# with open('save.blob', 'rb') as f:
    # data = f.read(16)
    # print('Read 16 bytes:', data)

    # while data:
        # decompressed_data = lzd.decompress(data)
        # if decompressed_data:
            # print('Decompressed: "{!r}"'.format(decompressed_data))

        # data = f.read(16)
        # print('Read 16 bytes:', data)

# Test LZMAFile
# with lzma.open('save.blob') as f:
    # print(f.read())
    
# Test Stream
# with open('save.blob', 'rb') as f:
    # print(lzma.decompress(f.read()))
    
# Test decompress
data = open('save.blob', 'rb').read()
print(lzma.decompress(data))
