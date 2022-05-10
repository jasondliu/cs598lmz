import lzma
# Test LZMADecompressor

def decompress(source):
    dec = lzma.LZMADecompressor()
    with open(source, "rb") as f:
        file_content = f.read()
        d = dec.decompress(file_content)
        print(d)

