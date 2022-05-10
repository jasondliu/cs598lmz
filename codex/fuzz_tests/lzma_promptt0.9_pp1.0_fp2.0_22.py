import lzma
# Test LZMADecompressor with various intervals and compare to reference
decomp = lzma.LZMADecompressor()
while True:
    final = False
    length = random.randrange(1000)
    print("reading", length, "bytes", end="")
    data = file.read(length)
    print("- %d bytes read" % len(data))
    if not data:
        break
    print("decompressing", len(data), "bytes", end="")
    if len(data) < 1024:
        final = True
    decomp_data = decomp.decompress(data, final)
    print("- %d bytes decompressed" % len(decomp_data))
    if decomp_data != ref[pos:pos + len(decomp_data)]:
        print("original:", ref[pos:pos + len(decomp_data)])
        print("decompress:", decomp_data)
        raise SystemExit("unexpected data in decompression")
    pos += len(decomp_data)

try:
    decomp.decompress("")
except EOFError
