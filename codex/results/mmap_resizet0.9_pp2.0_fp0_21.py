import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    try:
        m[1] = bytes(1)
    except ValueError as exc:
        print(exc)
</code>
Results: <code>mmap assignment out of range</code>

