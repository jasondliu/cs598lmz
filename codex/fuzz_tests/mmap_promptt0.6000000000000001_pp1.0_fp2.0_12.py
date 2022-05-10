import mmap
# Test mmap.mmap.rfind()

# Create a new file to mmap
with open(test.test_support.TESTFN, "wt") as f:
    f.write('\0' * 100)

with open(test.test_support.TESTFN, "r+b") as f:
    m = mmap.mmap(f.fileno(), 100)

    # Find a byte
    pos = m.rfind(b'\0')
    eq(pos, 99)

    # Find a substring
    pos = m.rfind(b'\0' * 50)
    eq(pos, 49)

    # Find a character not present
    pos = m.rfind(b'\1')
    eq(pos, -1)

    # Find an empty string
    pos = m.rfind(b'')
    eq(pos, 99)

    # Find outside the range
    pos = m.rfind(b'\0', 50)
    eq(pos, 49)

    # Find outside the range, with a step
    pos = m.rfind(
