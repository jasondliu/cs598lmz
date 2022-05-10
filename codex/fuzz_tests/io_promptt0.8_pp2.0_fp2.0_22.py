import io
# Test io.RawIOBase.readinto for arbitrary non-negative sizes
size = random.randint(0, sys.maxsize)
with open(support.TESTFN, 'w+b') as f:
    data = f.readinto(bytearray(size))
    f.seek(0)
# Test io.RawIOBase.readinto for zero size
with open(support.TESTFN, 'w+b') as f:
    data = f.readinto(bytearray(0))
    f.seek(0)
# Test io.RawIOBase.readinto for negative size
with open(support.TESTFN, 'w+b') as f:
    with self.assertRaises(ValueError):
        f.readinto(bytearray(-1))
    f.seek(0)
# Test io.RawIOBase.readinto for 1-byte buffer
with open(support.TESTFN, 'w+b') as f:
    for _ in range(100):
        f.write(b'@')
    f.seek(0)
    for i in range
