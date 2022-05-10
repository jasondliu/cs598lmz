import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
I expected an empty array, but I get a byte array <code>b'\x01'</code> instead.
How can I truncate the file and the mmap at the same time?


A:

The mmap object is not bound to the file descriptor. This is a different concern from being bound to the file's name.
If you open the file with <code>f = open('test', 'r+')</code> it will work fine.
You could then truncate the file like this:
<code>f.truncate(0)
</code>

Example:
<code>import mmap

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'a')
    f.truncate(0)
    print(m[:])
    m.close()
</code>
Output:
<code>b''
</code>

