import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.open('data/sample.bz2', 'rb') as input:
    with open('data/sample.out', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

# Test BZ2File

with bz2.open('data/sample.bz2', 'rb') as input:
    with open('data/sample.out', 'wb') as output:
        shutil.copyfileobj(input, output)
 
# Test BZ2File with context manager

with bz2.open('data/sample.bz2', 'rb') as input, open('data/sample.out', 'wb') as output:
    shutil.copyfileobj(input, output)
 
# Test BZ2File with compression

with bz2.open('data/sample.out.bz2', 'wb') as output:
    with open
