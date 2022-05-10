import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>.
How can I get <code>b'\x01'</code>?


A:

You can't.
When you truncate the file, the mmap object is no longer valid.  The bytes that were in the mmap object are gone.

