import bz2
bz2.BZ2File(file_name, 'r')

# Reading a text file line by line
with open(file_name, 'r') as f:
    print(f.readline())

# Iterating over the lines of a file
with open(file_name, 'r') as f:
    print(next(f))
    print(next(f))

# Writing data into a compressed file
data = np.arange(0, 100)
with bz2.BZ2File('array.bz2', 'w') as f:
    np.save(f, data)

# Reading data from a compressed file
with bz2.BZ2File('array.bz2', 'r') as f:
    data_new = np.load(f)
np.allclose(data, data_new)

# Reading a file in chunks
with open(file_name, 'r') as f:
    for line in f:
        print(line)

# Reading a file in chunks
with open(file_name, 'r') as f:

