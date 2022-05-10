import bz2
# Test BZ2Decompressor

with bz2.open("../data/sample_data/sample_data.bz2", "rb") as f:
    decompressor = bz2.BZ2Decompressor()
    for chunk in iter(lambda: f.read(100 * 1024), b''):
        data = decompressor.decompress(chunk)
        if data:
            print(data)

# Test BZ2File

with bz2.BZ2File("../data/sample_data/sample_data.bz2", "rb") as f:
    file_content = f.read()
    print(file_content)

# Test BZ2Compressor

uncompressed_data = b"Lots of content here"
compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(uncompressed_data)
print(compressed_data)

# Test compress

uncompressed_data = b"Lots of content here"
compressed_data = bz2.compress(uncompressed_data)
print(comp
