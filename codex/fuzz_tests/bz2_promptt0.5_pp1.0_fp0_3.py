import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()
filepath = '../data/enwiki-latest-pages-articles.xml.bz2'

with bz2.open(filepath, 'rb') as file:
    # Read the first 100 bytes
    first100_bytes = file.read(100)

    # Pass the first 100 bytes to the decompressor and decompress the rest
    rest_of_file = decompressor.decompress(first100_bytes)
    
    # Print the first 1000 bytes of the decompressed file
    print(rest_of_file[:1000])

# Test BZ2File

filepath = '../data/enwiki-latest-pages-articles.xml.bz2'

with bz2.open(filepath, 'rb') as file:
    # Print the first 1000 bytes
    print(file.read(1000))

# Test BZ2File with context manager

with bz2.open('../data/enwiki-latest-pages-articles.xml.bz2', 'rb') as file:
