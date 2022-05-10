import bz2
# Test BZ2Decompressor on a file

# Open the file
with bz2.open('example.bz2', 'rb') as input:
    print('File opened')

