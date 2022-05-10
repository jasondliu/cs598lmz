import lzma
# Test LZMADecompressor
comp = lzma.LZMACompressor()
with open('/tmp/test.lzma', 'wb') as out:
    out.write(comp.compress(b'foobar'))
    out.write(comp.flush())

with open('/tmp/test.lzma', 'rb') as inp:
    decomp = lzma.LZMADecompressor()
    print(decomp.decompress(inp.read()))

# Test LZMAFile
with lzma.open('/tmp/test.lzma', 'rb') as inp:
    print(inp.read())

with lzma.open('/tmp/test.lzma', 'wt', encoding='utf-8') as out:
    out.write('foobar')

with lzma.open('/tmp/test.lzma', 'rt', encoding='utf-8') as inp:
    print(inp.read())

os.remove('/tmp/test.lzma')
