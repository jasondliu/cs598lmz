import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/moby_dick.bz2') as input:
    with open('data/moby_dick.txt', 'wt') as output:
        for line in input:
            output.write(line.decode('utf-8'))
# Test BZ2Compressor

with open('data/moby_dick.txt', 'rt') as input:
    with bz2.BZ2File('data/moby_dick.bz2', 'wb') as output:
        for line in input:
            output.write(line.encode('utf-8'))
# Test BZ2Compressor with a buffer

with open('data/moby_dick.txt', 'rt') as input:
    with bz2.BZ2File('data/moby_dick.bz2', 'wb') as output:
        buffer = input.read(1024)
        while len(buffer) > 0:
            output.write(buffer.encode('utf-8'))
            buffer = input
