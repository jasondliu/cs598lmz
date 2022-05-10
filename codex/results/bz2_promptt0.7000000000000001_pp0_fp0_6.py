import bz2
# Test BZ2Decompressor
if True:
    with open("hg38.fa.bz2", "rb") as f:
        decompressor = bz2.BZ2Decompressor()
        with open("hg38.fa", "wb") as g:
            for block in iter(lambda: f.read(1024*1024*10), b''):
                g.write(decompressor.decompress(block))
# Test BZ2File
if True:
    with bz2.BZ2File("hg38.fa.bz2", "r") as f:
        with open("hg38.fa", "wb") as g:
            for block in iter(lambda: f.read(1024*1024*10), b''):
                g.write(block)
# Test bz2 library
if True:
    with open("hg38.fa", "wb") as g:
        with bz2.open("hg38.fa.bz2", "rb") as f:
            for block in iter(lambda: f.read(1024*1024*10), b''
