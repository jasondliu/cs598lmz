import lzma
# Test LZMADecompressor and LZMACompressor by compressing and
# decompressing bytes, bytearrays, and strings.

def lzma_compress(text):
    c = lzma.LZMACompressor()
    w = c.compress(text)
    w += c.flush()
    return w

def lzma_compress_fp(fp_src, fp_dst):
    c = lzma.LZMACompressor()
    size64 = int(os.path.getsize(fp_src) / 64)
    with open(fp_src, 'rb') as f:
        for i in range(size64):
            src = f.read(64)
            w = c.compress(src)
            w += c.flush()
            fp_dst.write(w)

def lzma_decompress(byte_data):
    dc = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO)
    w = dc.decompress(byte_data)
    return
