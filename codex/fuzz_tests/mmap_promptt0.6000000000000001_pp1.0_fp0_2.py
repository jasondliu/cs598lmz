import mmap
# Test mmap.mmap object.

# Try to open a file for writing.
with open('hello.txt', 'w+') as f:
    # Try to create the mmap.
    try:
        mm = mmap.mmap(f.fileno(), 0)
    except mmap.error:
        print 'Could not create mmap.'
        raise SystemExit
    # Print the mmap.
    print 'mm =', mm
    # Test mmap.write().
    mm.write('hello world')
    # Print the mmap.
    print 'mm =', mm
    # Test mmap.seek().
    mm.seek(0)
    # Test mmap.read().
    print 'mm.read() =', mm.read()
    # Test mmap.readline().
    mm.seek(0)
    print 'mm.readline() =', mm.readline()
    # Test mmap.readlines().
    mm.seek(0)
    print 'mm.readlines() =', mm.readlines()
    # Test mmap.tell().
    print 'mm.
