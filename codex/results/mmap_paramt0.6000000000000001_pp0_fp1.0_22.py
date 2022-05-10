import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
    m.close()
</code>
This works as expected (the byte at offset 0 is <code>2</code>).
But what if I want to use a <code>mmap</code> object as a context manager?
<code>with open('test', 'r+b') as f:
    with mmap.mmap(f.fileno(), 0) as m:
        m.write(bytes(2))
        m.seek(0)
        print(m.read(1))
</code>
This doesn't work, because the <code>mmap</code> object is closed before I can read from it.
I could do something like this:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    try:
        m.write(bytes(2))
        m.seek(0)
        print(m.read(1))
    finally:

