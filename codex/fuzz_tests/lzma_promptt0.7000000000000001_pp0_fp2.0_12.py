import lzma
# Test LZMADecompressor

def decompress(source):
    dec = lzma.LZMADecompressor()
    with open(source, "rb") as f:
        file_content = f.read()
        d = dec.decompress(file_content)
        print(d)

decompress('log.xz')

# Test LZMACompressor
def compress(source):
    comp = lzma.LZMACompressor()
    with open(source, "rb") as f:
        file_content = f.read()
        c = comp.compress(file_content)
        print(c)
        print(comp.flush())

compress('log.txt')

# Test LZMAFile - compress

def compress(source, dest):
    with lzma.open(dest, "wb") as f:
        with open(source, "rb") as s:
            f.write(s.read())

compress('log.txt', 'log1.xz')

# Test LZMAFile - decompress

def decomp
