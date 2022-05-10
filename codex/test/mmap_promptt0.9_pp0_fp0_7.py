import mmap
# Test mmap.mmap.flush

data = "abcd"

f = open("/dev/zero", "w+")
f.seek(len(data))
f.write("x")

mm = mmap.mmap(f.fileno(), 4)

