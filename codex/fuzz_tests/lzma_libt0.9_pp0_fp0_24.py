import lzma
lzmadecode = lzma._decompressobj(lzma.FORMAT_RAW, None, 0)
xzdecode = lzmadecode.decompress

def xzdecode_file(path):
    with open(path, 'rb') as f:
        decomp = lzmadecode.copy()
        for chunk in iter(lambda: f.read(io.DEFAULT_BUFFER_SIZE), b''):
            yield decomp.decompress(chunk)
        yield decomp.flush()
</code>

