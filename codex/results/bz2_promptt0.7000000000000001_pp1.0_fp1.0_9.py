import bz2
# Test BZ2Decompressor()
# Decompress a file compressed by bzip2. 

with bz2.BZ2File('class.py.bz2', 'rb') as input:
    with open('class.py.bz2.out', 'wb') as output:
        for data in iter(lambda: input.read(100 * 1024), b''):
            output.write(data)
