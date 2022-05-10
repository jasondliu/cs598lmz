import bz2
bz2.decompress(compressed_data)

compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# Compress a file
with open('filename.txt', 'rb') as input:
    with bz2.open('filename.txt.bz2', 'wb') as output:
        output.writelines(input)

# Decompress a file
with bz2.open('filename.txt.bz2', 'rb') as input:
    with open('filename.txt', 'wb') as output:
        for line in input:
            output.write(line)

# Compress a file using a context manager
with bz2.open('filename.txt.bz2', 'wb') as output:
    with open('filename.txt', 'rb') as input:
        output.writelines(input)

# Decompress a file using a context manager
with bz2.open('filename.txt.bz2', 'rb') as input:
    with open('filename.txt', 'wb
