import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(bz2_data)

# Decompress and read the entire file
with bz2.open('example.bz2', 'rt') as input:
    text = input.read()

# Read the first 10 bytes
with bz2.open('example.bz2', 'rt') as input:
    first_ten_bytes = input.read(10)

# Read one line
with bz2.open('example.bz2', 'rt') as input:
    first_line = input.readline()

# Iterate over lines
with bz2.open('example.bz2', 'rt') as input:
    for line in input:
        print(line)

# Write to a compressed file
with bz2.open('example.bz2', 'wt') as output:
    output.write(text)

# Write a compressed file with compression level 9
with bz2.open('example.bz2', 'wt', compresslevel=
