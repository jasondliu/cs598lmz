import mmap
# Test mmap.mmap()
m = mmap.mmap(0, 0, "sharedmem")
m.write("Hello world!\n")
print "Read from mmap: %s" % m.read(14)
print "Closing mmap..."
m.close()
print "Done."
