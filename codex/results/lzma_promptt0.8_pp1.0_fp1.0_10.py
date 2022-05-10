import lzma
# Test LZMADecompressor()

decompressor = lzma.LZMADecompressor()

# decompress_func = decompressor.decompress

# while True:
#     chunk = decompress_func()
#     if chunk == b'':
#         break
#     print(chunk)

# Test LZMADecompressor.decompress(data, max_length=-1)


decompressor = lzma.LZMADecompressor()

with lzma.open('python.xz', mode='rb') as input, \
        open('python.txt', mode='wb') as output:
    
    for buf in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(buf))

    output.write(decompressor.flush())
# Test compressfile()

with lzma.open(
            'python.xz', 
            mode='wb', 
            format=lzma.FORMAT_XZ, 
            preset=9
            ) as output:
