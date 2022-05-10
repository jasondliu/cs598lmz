import mmap
# Test mmap.mmap(0,1)

# from test_mmap import size
size = 10*1024*1024

verbose = 1

f = open("foo.txt", "w+b")
f.write(b"a" * size)
f.close()

if verbose:
    print("\nopening foo.txt for writing...")
f = open("foo.txt", "r+")
m = mmap.mmap(f.fileno(), 0)
if verbose:
    print("mmap created: start=%s, length=%s" % (m.tell(), m.size()))

if verbose:
    print("writing to mmap...")
n = m.write(b'b'*1000)
if verbose:
    print("wrote %s bytes" % n)

if verbose:
    print("reopening mmap...")
m.close()
m = mmap.mmap(f.fileno(), 0)
if verbose:
    print("mmap reopened: start=%s, length=%s" % (m.
