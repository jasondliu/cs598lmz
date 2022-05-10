import mmap
# Test mmap.mmap:
f=open("test", "w")
for i in range(10):
    f.write((chr(65+i)*mmap.ALLOCATIONGRANULARITY) + "\n")
f.close
f=open("test", "r+b")
print repr(mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ))
print repr(mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ, access=mmap.ACCESS_READ))
print repr(mmap.mmap(f.fileno(), 0, prot=mmap.PROT_WRITE))
print repr(mmap.mmap(f.fileno(), 0, prot=mmap.PROT_WRITE, access=mmap.ACCESS_WRITE))
# This should fail (read-only file)
try:
    print repr(mmap.mmap(f.fileno(), 0, prot=mmap.PROT_WRITE|mmap.PROT_EXEC))
except:
    print "read-
