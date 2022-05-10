import lzma
# Test LZMADecompressor.readto() and LZMADecompressor.read1()

for fname in glob.glob("testdata/*.xz"):
    with open(fname, "rb") as f:
        cdata = f.read()
    with lzma.open(fname, "rb") as g:
        try:
            data = g.read()
        except:
            data = None
        if data is not None:
            assert data == cdata
        #
        data = b""
        while True:
            try:
                chunk = g.read1(0x10000)
            except:
                chunk = None
            if chunk is None or not chunk:
                break
            data += chunk
        assert data == cdata
    with lzma.LZMADecompressor() as decomp:
        data = b""
        while True:
            try:
                chunk = cdata[decomp.unused_data_offset:]
                if not chunk:
                    break
                try:
                    data += decomp.decompress(chunk, 0x10000
