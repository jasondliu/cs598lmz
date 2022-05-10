import bz2
bz2.decompress(compressed)

# Compress a file
with open('file.txt', 'rb') as input:
    with bz2.BZ2File('file.txt.bz2', 'wb') as output:
        output.writelines(input)

# Decompress a file
with bz2.BZ2File('file.txt.bz2', 'rb') as input:
    with open('file.txt', 'wb') as output:
        for line in input:
            output.write(line)

# Compress a file and read it as a stream
with open('file.txt', 'rb') as input:
    with bz2.BZ2File('file.txt.bz2', 'wb') as output:
        output.writelines(input)

with bz2.BZ2File('file.txt.bz2', 'rb') as input:
    for line in input:
        print(line)

# Compress a file and read it as a stream in chunks
with open('file.txt', 'rb') as
