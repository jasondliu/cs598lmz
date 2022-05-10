import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

# Read in the compressed file
with bz2.BZ2File('example.bz2', 'rb') as input:
    # Decompress the file
    with open('uncompressed_file.txt', 'wb') as output:
        for data in iter(lambda : input.read(100 * 1024), b''):
            output.write(decompressor.decompress(data))

# Print out the contents of the uncompressed file
with open('uncompressed_file.txt', 'rb') as f:
    print(f.read())

# Clean up the decompressor
decompressor.flush()

# Clean up the files
os.remove('example.bz2')
os.remove('uncompressed_file.txt')

# <script.py> output:
#     b'some text\n'
