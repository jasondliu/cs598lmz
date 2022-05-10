import mmap
# Test mmap.mmap(fileno,0,prot=mmap.PROT_WRITE)
# Called in the form:
# python tmp_read.py /home/brandon/sample1.txt

# For reading the contents of a file using the mmap module
f = open(sys.argv[1],'r+b')
size = os.path.getsize(sys.argv[1])
contents = mmap.mmap(f.fileno(), size, prot=mmap.PROT_WRITE)
contents[:] = "foobar\n"
l = len(contents)
print "length: %s" % l
print contents[:5]
