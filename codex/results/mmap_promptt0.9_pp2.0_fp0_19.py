import mmap
# Test mmap.mmap
print("mmap.mmap config:{}\n".format(str(mmap.mmap)))
mmap.mmap(0, 10000000)
# Test page size
print("mmap.PAGESIZE:{}".format(repr(mmap.PAGESIZE)))
# Test access modes
for a in [mmap.ACCESS_READ, mmap.ACCESS_WRITE, mmap.ACCESS_COPY]:
    try:
        mmap.mmap(0, 100000, access=a)
    except mmap.error as e:
        print("mmap.mmap config:{}\n".format(str(e)))

# Test flags
print("Known FLAGS:{}".format(repr(mmap.MAP_PRIVATE)))

# Test files
try:
    f = open('/dev/mem', 'r')
except:
    # pyboard
    f = open('/flash/example_memory.py', 'r')
m = mmap.mmap(f.fileno(), 0)
print("m.flags:{}".format
