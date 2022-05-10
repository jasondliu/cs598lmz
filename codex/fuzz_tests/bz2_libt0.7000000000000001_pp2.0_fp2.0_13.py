import bz2
bz2.BZ2File('data.bz2')

# the 'with' statement is used when working with unmanaged resources
#   - it automatically releases the resource when the block is exited

# another example
with bz2.BZ2File('data.bz2') as f:
    data = f.read()

# the 'with' statement is used when working with unmanaged resources
#   - it automatically releases the resource when the block is exited

# another example
with bz2.BZ2File('data.bz2') as f:
    for line in f:
        print(line)


# EXERCISE: use the glob module to list all the files in a directory
#           print the filenames sorted by size

# ANSWER
import glob
import os

# glob module
files = glob.glob('*.py')

# sort the files by size
files.sort(key=lambda name: os.path.getsize(name))

print(files)


# EXERCISE: write a program that walks a directory tree and prints
#           the
