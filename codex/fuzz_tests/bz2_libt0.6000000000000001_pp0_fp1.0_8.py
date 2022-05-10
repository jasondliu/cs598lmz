import bz2
bz2.decompress(sample_bz2)

# Decompress the file and store the result.

with open('sample.bz2', 'rb') as f:
    data = bz2.decompress(f.read())

# Write the data to a new file.

with open('sample.txt', 'wb') as f:
    f.write(data)

# Open the file for reading.

with open('sample.txt', 'r') as f:
    print(f.read())
