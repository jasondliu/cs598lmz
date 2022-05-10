import mmap
# Test mmap.mmap()
with open('/tmp/foobar', 'wb') as f:
    f.write(os.urandom(1024))

mapf = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
os.remove('/tmp/foobar')
len(mapf)

# Test msync
adjf = mmap.mmap(-1, 1000, access=mmap.ACCESS_WRITE)
adjf.write(os.urandom(1000))
adjf.close()

def test_anon():
    adjf = mmap.mmap(-1, 1000, access=mmap.ACCESS_WRITE)
    os.lseek(adjf.fileno(), 0, 0)
    adjf.write(os.urandom(1000))
    adjf.close()

start = time.time()
for i in xrange(100):
    test_anon()

