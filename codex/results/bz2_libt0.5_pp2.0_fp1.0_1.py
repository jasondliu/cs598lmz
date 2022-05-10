import bz2
bz2.decompress(compressed_data)

# Compress a file
import bz2

with open('file.txt', 'rb') as input:
    compressed_data = bz2.compress(input.read())

with open('file.bz2', 'wb') as output:
    output.write(compressed_data)

# Decompress a file
import bz2

with open('file.bz2', 'rb') as input:
    compressed_data = input.read()

with open('file.txt', 'wb') as output:
    output.write(bz2.decompress(compressed_data))

# Decompress a file without reading the entire thing into memory
import bz2

with bz2.open('file.bz2', 'rb') as input:
    for line in input:
        print(line)

# Compress a file using a context manager
import bz2

with bz2.open('file.bz2', 'wt') as output:
    output.write('Contents of
