from bz2 import BZ2Decompressor
BZ2Decompressor(['extra1', 'extra2'])
BZ2Decompressor()

with open('bzip2.tar', 'rb') as rf:
    with BZ2File('bzip2.tar.bz2', 'w') as wf:
        wf.writelines(rf)
    with BZ2File(wf.name, 'r') as rf2:
        with open('bzip2.tar.bz2.bz2', 'wb') as wf2:
            wf.writelines(rf2)

with open('bzip2.tar', 'rb') as rf:
    bz2c = BZ2Compressor()
    with open('bzip2.tar.bz2.bz2', 'wb') as wf:
        for line in rf:
            wf.write(bz2c.compress(line))
        wf.write(bz2c.flush())

with open('bzip2.tar', 'rb') as rf:
    bz2c = BZ2Compressor
