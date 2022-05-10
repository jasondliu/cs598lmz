import bz2
# Test BZ2Decompressor
with bz2.BZ2Decompressor() as decompressor:
    file_content = decompressor.decompress(compressed_content)
print(repr(file_content))

# Test BZ2File
with bz2.BZ2File(fileobj=BytesIO(compressed_content)) as bz_file:
    print(repr(bz_file.read()))

# Test BZ2File with context manager
with bz2.BZ2File(fileobj=BytesIO(compressed_content)) as bz_file:
    print(repr(bz_file.read()))

# BZ2File without context manager
bz_file = bz2.BZ2File(fileobj=BytesIO(compressed_content))
print(repr(bz_file.read()))
bz_file.close()

# Test BZ2File with filename
with bz2.BZ2File('lorem.txt.bz2') as bz_file:
    print(repr(bz_file.
