import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

with open('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as f:
    file_content = f.read()
    decompressed_data = decompressor.decompress(file_content)
    print(decompressed_data[:100])

# Test BZ2File
with bz2.BZ2File('data/enwiki-latest-pages-articles.xml.bz2', 'rb') as f:
    print(f.readline())

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressed_data = compressor.compress(b'This is a test')
compressed_data += compressor.flush()
print(compressed_data)

# Test BZ2File
with bz2.BZ2File('data/test.bz2', 'wb') as f:
    f.write(b'This is a test')

with bz2.BZ2File('data/test
