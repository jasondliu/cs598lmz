import lzma
# Test LZMADecompressor class

decomp = lzma.LZMADecompressor()

print('Testing LZMADecompressor')

# Test using read() and decompress()
# This works
lzdecomp = lzma.LZMADecompressor()

with gzip.open('../tests/data/lzma.gz', 'rb') as f:
    data = f.read()

lzdata = lzdecomp.decompress(data)
print(data[:100])
print(lzdata[:100])

# This doesn't
lzdecomp = lzma.LZMADecompressor()

with gzip.open('../tests/data/lzma.gz', 'rb') as f:
    data = f.read()

lzdata = decomp.read(data)
print(data[:100])
print(lzdata[:100])
</code>
I get the following output:
<code>$ python3 lzma-gzip-test.py
Testing LZMADecompressor
