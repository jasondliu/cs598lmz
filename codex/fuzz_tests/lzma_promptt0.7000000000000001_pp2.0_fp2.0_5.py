import lzma
# Test LZMADecompressor object
decompressor = lzma.LZMADecompressor()

with lzma.open('data/enwik8.xz') as infile:
    with open('data/enwik8_uncompressed', 'wb') as outfile:
        for buf in iter(lambda: infile.read(1024 * 1024), b''):
            outfile.write(decompressor.decompress(buf))
        outfile.write(decompressor.flush())
 
with open('data/enwik8_uncompressed', 'rb') as f:
    data = f.read()

print(data[0])
print(data[:10000])

print(data[-1])
print(data[-10000:])

# Test LZMAFile object
with lzma.open('data/enwik8.xz') as f:
    data = f.read()
    print(data[:10000])
    print(data[-10000:])
 
with lzma.open('data/enwik8.xz', mode='rt',
