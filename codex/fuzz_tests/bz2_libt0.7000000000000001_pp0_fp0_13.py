import bz2
bz2.BZ2File()

# We can read the file one line at a time
with bz2.BZ2File('data/small.bz2', 'r') as f:
    print(f.readline())
    print(f.readline())

# We can also do the same with context managers
# (This is the preferred method, because it cleans up the file handle for us)
with bz2.BZ2File('data/small.bz2', 'r') as f:
    print(next(f))
    print(next(f))

# We can also read the entire file into memory
with bz2.BZ2File('data/small.bz2', 'r') as f:
    file_content = f.read()
    print(file_content)

# We can also read the file into a list
# (Each list element is one line)
with bz2.BZ2File('data/small.bz2', 'r') as f:
    file_content = list(f)
    print(file_content)

