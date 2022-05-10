import lzma
# Test LZMADecompressor
with lzma.open('enwik8.xz') as src, open('enwik8.unxz','wb') as dst:
    decomp = lzma.LZMADecompressor()
    while True:
        data = src.read(1024)
        if not data:
            break
        dst.write(decomp.decompress(data))
 
with open('enwik8.unxz', 'rb') as f:
    text = f.read()
print(text[:20])

# Test LZMAEncoder
with open('enwik8.unxz', 'rb') as src, lzma.open('enwik8.xz', 'wb') as dst:
    encoder = lzma.LZMAEncoder()
    while True:
        data = src.read(1024)
        if not data:
            break
        dst.write(encoder.encode(data))
 
with lzma.open('enwik8.xz') as f:
    text = f.read()
print(text[
