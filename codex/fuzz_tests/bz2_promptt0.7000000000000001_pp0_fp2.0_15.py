import bz2
# Test BZ2Decompressor

with bz2.BZ2File('sample.bz2') as f:
    data = f.read()
# Test BZ2File

with bz2.BZ2File('sample.bz2') as f:
    for line in f:
        print(line)
# Test BZ2File.__init__

with bz2.BZ2File('sample.bz2') as f:
    pass
# Test BZ2File.close

with bz2.BZ2File('sample.bz2') as f:
    f.close()
# Test BZ2File.flush

with bz2.BZ2File('sample.bz2') as f:
    f.flush()
# Test BZ2File.name

with bz2.BZ2File('sample.bz2') as f:
    print(f.name)
# Test BZ2File.read

with bz2.BZ2File('sample.bz2') as f:
    print(f.read(1))

