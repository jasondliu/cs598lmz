import bz2
bz2.BZ2File(path, 'r')

# Compress a file
with open('file.txt', 'rb') as inp, bz2.BZ2File('file.txt.bz2', 'wb') as out:
    out.writelines(inp)

# Decompress a file
with bz2.BZ2File('file.txt.bz2', 'rb') as inp, open('file.txt', 'wb') as out:
    for line in inp:
        out.write(line)

# Compress a file after reading it
with open('file.txt', 'rb') as inp, bz2.BZ2File('file.txt.bz2', 'wb') as out:
    out.write(inp.read())

# Decompress a file after reading it
with bz2.BZ2File('file.txt.bz2', 'rb') as inp, open('file.txt', 'wb') as out:
    out.write(inp.read())
