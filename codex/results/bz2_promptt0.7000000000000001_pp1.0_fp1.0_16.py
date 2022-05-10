import bz2
# Test BZ2Decompressor on data generated with command:
# python -c "import bz2, sys; bz2.BZ2Compressor(9).compress(sys.stdin.read())"
data = open('lorem.txt', 'rb').read()
cdata = bz2.compress(data, 9)
bz2.decompress(cdata)

d = bz2.BZ2Decompressor()
d.decompress(cdata)

d.unused_data

d.decompress(b'BZh91AY&SY')
d.unused_data

d.decompress(b'BZh91AY&SY')
d.unused_data

d.decompress(b'')
d.unused_data

d.decompress(cdata)
d.decompress(b'BZh91AY&SY')

try:
    d.decompress(b'AY&SY')
except EOFError:
    pass

d.decompress(b'BZh91AY&
