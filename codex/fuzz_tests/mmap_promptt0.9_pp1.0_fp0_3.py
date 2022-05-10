import mmap
# Test mmap.mmap
# example: python mmap_test.py <filename> <offset> <string>

def main():
    fname = sys.argv[1]
    try:
        off = int(sys.argv[2])
    except (ValueError):
        print 'Offset is not numeric: %s' % (sys.argv[2])
        return
#    try:
        # Create file
    fout=open(fname, "w+")
    # write the file
    fout.write("abcde\n")
    print "Wrote: abcde"
    fout.seek(0)
        # reopen the file with mmap
    fin = mmap.mmap(fout.fileno(), 0)
    s=sys.argv[3]
    print "Changing '%s' to '%s'" % (fin[off], s)
    fin[off] = s
    fin.close()
    fout.close()
    print "Look at: %s" % (fname)
#    except (IOError,ValueError):

