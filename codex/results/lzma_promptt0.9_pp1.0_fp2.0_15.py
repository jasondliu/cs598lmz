import lzma
# Test LZMADecompressor

with open('sorted.json.xz', 'rb') as lzma_file:
    lzma_decompressor = lzma.LZMADecompressor()
    with open('sorted.json', 'w') as json_file:
        for block in iter(lambda: lzma_file.read(64 * 1024), b''):
            json_file.write(lzma_decompressor.decompress(block))
        json_file.write(lzma_decompressor.flush())
with open('sorted.json.xz', 'rb') as lzma_file:
    lzma_decompressor = lzma.LZMADecompressor()
    with open('sorted.json', 'w') as json_file:
        chunk = lzma_file.read(64 * 1024)
        output = lzma_decompressor.decompress(chunk)
        while output != b'':
            json_file.write(output)
            chunk = lzma_file.read(64 *
