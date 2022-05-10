import mmap
# Test mmap.mmap
with open(filename,'r+b') as f:
    # memory-map the file, size 0 means whole file
    map = mmap.mmap(f.fileno(), 0)
    print "Original")
    read_file(filename)
    print "After mmap.read(3)"
    map.readable(3)
    read_file(filename)
    print "After mmap.write(b'mun')"
    map.write(b'mun')
    read_file(filename)
    map.close()
</code>

