import bz2
# Test BZ2Decompressor class
with open('py3k.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    with open('py3k.tar', 'wb') as g:
        while True:
            block = f.read(1024)
            if not block:
                break
            g.write(decompressor.decompress(block))
        g.write(decompressor.flush())

# Test BZ2File class
with bz2.BZ2File('py3k.bz2', 'rb') as f:
    with open('py3k.tar', 'wb') as g:
        while True:
            block = f.read(1024)
            if not block:
                break
            g.write(block)

with bz2.BZ2File('py3k.bz2', 'rb') as f:
    f.read()

with bz2.BZ2File('py3k.bz2', 'rb') as f:
    f.read(10)

with
