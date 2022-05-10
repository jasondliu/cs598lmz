import bz2
# Test BZ2Decompressor
f = bz2.open("bigwiki/AA/wiki_00", 'r')
decomp = bz2.BZ2Decompressor()
for _ in range(2):
    data = f.read(100)
    print(decomp.decompress(data))
f.close()

# Test BZ2File
with bz2.BZ2File("bigwiki/AA/wiki_00") as f:
    data = f.read(100)
    print(data)
    data = f.read(100)
    print(data)
