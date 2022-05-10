import bz2
# Test BZ2Decompressor
with bz2.open('data/sample.bz2', 'rb') as f:
    decomp = bz2.BZ2Decompressor()
    while True:
        comp = f.read(16)
        if not comp:
            break

        print(decomp.decompress(comp))

# Test BZ2Compressor
decomp = bz2.BZ2Decompressor()
with bz2.open('data/sample.bz2', 'rb') as f:
    file_content = f.read()

assert decomp.decompress(file_content) == decomp.decompress(file_content)


def compress(str):
    return bz2.compress(str.encode('utf-8'))


def decompress(str):
    return bz2.decompress(str).decode('utf-8')


assert 'hello' == decompress(compress('hello'))

# Compress a file
with open('data/sample.bz2', 'rb') as sample_file:
    file_
