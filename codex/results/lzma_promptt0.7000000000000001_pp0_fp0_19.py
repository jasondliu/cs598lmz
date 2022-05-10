import lzma
# Test LZMADecompressor

f = open('lzma.lzma', 'rb')
fd = lzma.LZMADecompressor()

while True:
    buf = f.read(16 * 1024)
    if not buf:
        break
    data = fd.decompress(buf)
    if data:
        sys.stdout.write(data)
</code>

