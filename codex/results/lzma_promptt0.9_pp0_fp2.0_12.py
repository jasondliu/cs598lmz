import lzma
# Test LZMADecompressor()
with open('./7zr.exe', 'rb') as input, \
        lzma.open('./7zr_lzma.bin', 'wb') as output:
    output.write(input.read())

with open('./7zr.exe', 'rb') as input:
    # print(input.read(0))
    decompressor = lzma.LZMADecompressor(lzma.FORMAT_RAW, filters=[
        {'id': lzma.FILTER_LZMA1, 'dict_size': 229376, 'lc': 3, 'lp': 0, 'pb': 2, 'mode': lzma.MODE_FAST}])
    output = b''
    while True:
        chunk = input.read(50)
        if not chunk:
            break
        output += decompressor.decompress(chunk)
        # print(len(input.read(1)))

with open('./7zr_py.exe', 'wb') as f:
    f.write(output)


