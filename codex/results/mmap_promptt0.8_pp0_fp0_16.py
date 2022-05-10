import mmap
# Test mmap.mmap()

def test(filename):

    try:
        f = open(filename, "r+b")
    except IOError, e:
        print "Couldn't find specified file: ",filename
        return

    # memory-map the file, size 0 means whole file
    m = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print "Read original file contents: ", m.size(),"bytes"

    # print contents
    print m.read(10)

    # read into different variable using slice notation
    slice = m[:5]
    print "First 5 characters of file as read via slice: ", slice

    # update content using slice notation;
    # note that new content must have same size
    m[6:] = " world!\n"

    # ... and read again using regular method
    m.seek(0)
    print "Read entire file after mmap slice modification: ", m.readline()

    # close the map
    m.close()

    # close the file
    f.close()

if __name__
