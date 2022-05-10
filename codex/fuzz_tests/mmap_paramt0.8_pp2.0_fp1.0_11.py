import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1024)
    print(type(m), len(m), file=sys.stderr)
    print(m[:], file=sys.stderr)

    m[:] = bytes(100)
    print(m[:], file=sys.stderr)

    m.resize(1024)
    print(m[:], file=sys.stderr)
