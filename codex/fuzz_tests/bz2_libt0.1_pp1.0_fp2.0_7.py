import bz2
bz2.decompress(bz2_data)

# bz2.BZ2File
bz2_file = bz2.BZ2File('example.bz2')
print(bz2_file.read())
bz2_file.close()

# bz2.compress()
uncompressed_data = b'This is the original text.'
compressed_data = bz2.compress(uncompressed_data)
print(compressed_data)

# bz2.decompress()
original_data = bz2.decompress(compressed_data)
print(original_data)

# bz2.open()
with bz2.open('example.bz2', 'rt') as input:
    print(input.read())

# bz2.open()
with bz2.open('example.bz2', 'wt') as output:
    output.write('Contents of the example file go here.\n')

# bz2.open()
with bz2.open('example.b
