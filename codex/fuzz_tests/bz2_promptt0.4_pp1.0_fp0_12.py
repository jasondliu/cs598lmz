import bz2
# Test BZ2Decompressor
with bz2.BZ2File('sample.bz2') as f:
    with io.TextIOWrapper(f, encoding='utf-8') as dec:
        print(dec.read())

# Test BZ2Compressor
with open('sample.txt', 'rt') as f:
    data = f.read()

with bz2.BZ2File('sample.bz2', 'w') as f:
    f.write(data.encode('utf-8'))

with bz2.BZ2File('sample.bz2') as f:
    with io.TextIOWrapper(f, encoding='utf-8') as dec:
        print(dec.read())
 
# Test BZ2Compressor with a buffered writer
with open('sample.txt', 'rt') as f:
    data = f.read()

buf = io.BytesIO()
with bz2.BZ2Compressor(9) as comp:
    with io.BufferedWriter(comp, 1000) as f:
        f.write
