import bz2
bz2.decompress(compressed_data)

# Compress a file
with open('file.txt', 'rb') as input:
    with bz2.BZ2File('file.txt.bz2', 'wb') as output:
        output.writelines(input)

# Decompress a file
with bz2.BZ2File('file.txt.bz2', 'rb') as input:
    with open('file.txt', 'wb') as output:
        for line in input:
            output.write(line)

# Compress a file using a context manager
with bz2.BZ2File('file.txt.bz2', 'wb') as output:
    with open('file.txt', 'rb') as input:
        output.writelines(input)

# Decompress a file using a context manager
with open('file.txt', 'wb') as output:
    with bz2.BZ2File('file.txt.bz2', 'rb') as input:
        for line in input:
            output.write(line
