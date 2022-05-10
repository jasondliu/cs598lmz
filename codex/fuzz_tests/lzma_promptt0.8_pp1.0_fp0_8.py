import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()

with open('n' + str(i) + '.txt.xz', 'rb') as inp, open('n' + str(i) + '.txt', 'wb') as out:
    for buf in iter(partial(inp.read, 128), b''):
        data = decomp.decompress(buf)
        if data:
            out.write(data)
        else:
            raise lzma.LZMAError("Compressed file ended before the end-of-stream marker was reached")
# Extract the contents of all compressed files
for i in range(1, 5):
    decomp = lzma.LZMADecompressor()
    with open('n' + str(i) + '.txt.xz', 'rb') as inp, open('n' + str(i) + '.txt', 'wb') as out:
        for buf in iter(partial(inp.read, 128), b''):
            data = decomp.decompress(buf)
            if data:
                out.
