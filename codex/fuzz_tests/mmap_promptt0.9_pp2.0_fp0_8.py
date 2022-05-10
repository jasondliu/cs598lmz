import mmap
# Test mmap.mmap for large files
# This is important for CloudN.
# But this does not work, 2.6b1 uses the file-based mmap.mmap.

def test1():
    f = open('test.dat', 'wb')
    try:
        mapl = mmap.mmap(f.fileno(), 0)

        size = 100 * 1024 * 1024                       # hundred megs
        mapl.resize(size)
#        mapl.seek(0)
        print "Seeking to size-1"
        mapl.seek(size-1)

        mapl.write('\0')
        print "Seeking to size-2"
        mapl.seek(size-2)
        print "Writing 0 to mapl[-1]"
        mapl[-1] = '\0'
        print "Seeking to size-2"
        mapl.seek(size-2)
        print "Writing 0 to mapl[100]"
        mapl[100] = '\0'
    finally:
        f.close()
    return True

def test
