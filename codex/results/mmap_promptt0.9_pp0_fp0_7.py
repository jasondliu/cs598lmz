import mmap
# Test mmap.mmap.flush

data = "abcd"

f = open("/dev/zero", "w+")
f.seek(len(data))
f.write("x")

mm = mmap.mmap(f.fileno(), 4)

if mm.read(4) != data:
	print "First read failed"
	sys.exit(1)

mm.seek(1)
mm.write("K")
mm.flush()
f.flush()

f.seek(0)
if f.read(5) != "aKcdx":
	print "Flush failed"
	sys.exit(1)

mm.seek(1)
mm.write("L")
f.flush()
f.seek(0)
if f.read(5) != "aKcdx":
	print "Explicit flush failed"
	sys.exit(1)


#Test mmap.mmap.move

f = open("/dev/zero", "w+")
f.seek(4)
f.write("x")

mm = mmap
