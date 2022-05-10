import mmap
# Test mmap.mmap(fileno, length) constructor on invalid length arg

# Create a file and open it
with open('02.mmapfile', 'w+') as f:
    f.write('foo')
with open('02.mmapfile', 'r+') as f:
    # Test a negative length
    try:
        mmap.mmap(f.fileno(), -1)
    except ValueError:
        print('ValueError')
    # Test a length larger than the file size
    try:
        mmap.mmap(f.fileno(), 10)
    except ValueError:
        print('ValueError')
    # Test a length equal to the file size
    mmap.mmap(f.fileno(), 3)

os.unlink('02.mmapfile')
