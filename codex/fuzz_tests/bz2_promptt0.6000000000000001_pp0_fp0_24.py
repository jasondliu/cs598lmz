import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(compressed_data)
result == original_data

# Test BZ2File
with bz2.BZ2File('spam.bz2', 'wb') as output:
    with open('spam.txt', 'rb') as input:
        output.write(input.read())
# bz2.BZ2File is a binary file object
with bz2.BZ2File('spam.bz2', 'rb') as input:
    print(input.read(100))

# bz2.open is a text file object
with bz2.open('spam.bz2', 'rt') as input:
    print(input.read(100))
# bz2.BZ2File is a binary file object
with bz2.BZ2File('spam.bz2', 'rb') as input:
    print(input.read(100))

# bz2.open is a text file object
with bz2.
