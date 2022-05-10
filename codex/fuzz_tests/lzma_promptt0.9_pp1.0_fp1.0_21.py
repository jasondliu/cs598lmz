import lzma
# Test LZMADecompressor as a decompression text stream
buf = array.array("B", lzma.compress("Hello, world! *" * 1024 * 1024))
with lzma.LZMADecompressor(lzma.FORMAT_RAW, None, None) as decomp:
    with io.TextIOWrapper(io.BufferedReader(decomp, 64 * 1024), "utf-8") as wrapper:
        data = wrapper.read(32)
        data += wrapper.read(32)
        data += wrapper.read()
        data += wrapper.readline()
        data += wrapper.read(512)
        data += wrapper.readline()
        data += wrapper.read(1024)
        data += wrapper.readline()
        data += wrapper.read(8192)
        data += wrapper.readline()
        data += wrapper.read()
        data += wrapper.readline()
        data += wrapper.read()
        data += wrapper.readline()
        wrapper.seek(0)
        data += wrapper.read()
        data += wrapper.readline()
        data += wrapper.read
