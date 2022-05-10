import bz2
bz2.BZ2File(filename)

# Reading from a compressed file
with bz2.BZ2File(filename) as file:
    data = file.read()

# Writing to a compressed file
with bz2.BZ2File(filename, 'w') as file:
    file.write(data)

# Closing a file
file.close()

# Closing a file automatically
with bz2.BZ2File(filename) as file:
    do_something(file)

# Reading a compressed file in chunks
with bz2.BZ2File(filename) as file:
    for chunk in iter(lambda: file.read(100 * 1024), b''):
        data += chunk

# Reading a compressed file line by line
with bz2.BZ2File(filename) as file:
    for line in file:
        data += line

# Reading a compressed file line by line in chunks
with bz2.BZ2File(filename) as file:
    for chunk in iter(lambda: file.readline(100 * 1024), b''):

