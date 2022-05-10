import lzma
# Test LZMADecompressor.
decompressor = lzma.LZMADecompressor()
with open("output.xz", "rb") as input, open("output.dat", "wb") as output:
    while True:
        chunk = input.read(1024)
        if not chunk:
            break
        output.write(decompressor.decompress(chunk))
</code>

