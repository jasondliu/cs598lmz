import lzma
# Test LZMADecompressor and LZMACompressor

def t_decomp(data):
    dc = lzma.LZMADecompressor()
    data = dc.decompress(data)
    if len(dc.unused_data) > 0:
        print("unused data", repr(dc.unused_data))
    print("len(data)", len(data))

with open("archlinux-2016.05.01-dual.iso.lzma", "rb") as f:
    header = f.read(lzma.lzma_headers.LZMA_PROPS_SIZE)
    props = lzma.lzma_headers.decode_lzma_properties(header)
    data = f.read()
    t_decomp(header + data)
    t_decomp(data)

    c = lzma.LZMACompressor(format=lzma.FORMAT_RAW, filters=props)
    d = c.compress(data)
    t_decomp(d)

with open("/boot/vm
