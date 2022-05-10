import lzma
lzma.LZMADecompressor()
from zlib import decompress

def test(compress):
    d = {}
    d2 = {}
    i = 0
    for l in open(compress):
        i += 1
        if i < 600000:
            continue
        key = l[:l.find(' ')]
        d[key] = l[l.find(' ') + 1:]
        if i % 10000 == 0:
            print(i)
    #compress = open(compress, 'rb').read()
    #dcompressed = decompress(compress)
    #for l in dcompressed.split('\n'):
    #    if len(l) < 5:
    #        continue
    #    key = l[:l.find(' ')]
    #    v = l[l.find(' ') + 1:]
    #    d2[key] = v
    #for key in list(d):
    #    assert d[key] == d2[key]
    print('len', len(d))

   
