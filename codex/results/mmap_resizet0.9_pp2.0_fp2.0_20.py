import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    # One would expect m to be empty after truncate,
    # but instead it contains these bytes.
    # Much of the mmap documentation is phrased
    # ambiguously and hard to read, but I'm guessing
    # this was the intended design. It does however
    # require a little special handling code afterwards,
    # to ensure that one's memory view is indeed truncated
    # to the file size.
    print(repr(a))
    m.resize(0)
    m.close()
</code>

