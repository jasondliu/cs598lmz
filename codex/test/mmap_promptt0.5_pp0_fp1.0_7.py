import mmap
# Test mmap.mmap.read_byte()

f = open(os.path.join(os.path.dirname(__file__), 'mmap_data'), 'rb')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# Read the whole thing
assert m.read_byte() == ord('a')
assert m.read_byte() == ord('b')
assert m.read_byte() == ord('c')
assert m.read_byte() == ord('d')
assert m.read_byte() == ord('e')
assert m.read_byte() == ord('f')
assert m.read_byte() == ord('g')
assert m.read_byte() == ord('h')

# Read past the end
try:
    m.read_byte()
except ValueError:
    pass
else:
    raise Exception("expected ValueError")

# Read past the end (again)
try:
    m.read_byte()
except ValueError:
    pass
else:
    raise Exception("expected ValueError")


