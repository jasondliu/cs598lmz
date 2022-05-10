import bz2
# Test BZ2Decompressor
c = bz2.BZ2Compressor()
with open('pg20000.txt', 'rb') as rf:
    with open('pg20000.bz2', 'wb')as wf:
        while True:
            block = rf.read(64)
            if not block:
                break
            wf.write(c.compress(block))
c.flush()
# bz2.decompress(b)
# bz2.BZ2Decompressor()

d = bz2.BZ2Decompressor()
with open('pg20000.bz2', 'rb') as rf:
    with open('pg20000-restored.txt', 'wb') as wf:
        while True:
            block = rf.read(64)
            if not block:
                break
            wf.write(d.decompress(block))

# bz2.open(name, mode='r', buffering=1)
