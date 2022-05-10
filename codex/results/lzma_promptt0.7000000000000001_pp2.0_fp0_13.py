import lzma
# Test LZMADecompressor
decompress = lzma.LZMADecompressor()

with open('data/example.xz', 'rb') as input:
    file_content = input.read()
    data = decompress.decompress(file_content)
    print(data.decode('utf-8'))

print(decompress.eof)

decompress = lzma.LZMADecompressor()
try:
    decompress.decompress(b"garbage")
except EOFError:
    print("EOF")

print(decompress.eof)


# Test LZMACompressor
compress = lzma.LZMACompressor(lzma.FORMAT_XZ)

with open('data/example.xz', 'rb') as input, open('data/example.xz.copy', 'wb') as output:
    while True:
        block = input.read(64 * 1024)
        if not block:
            break
        output.write(compress.compress(block))
    output.
