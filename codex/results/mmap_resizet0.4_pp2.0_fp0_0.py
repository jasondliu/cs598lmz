import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect <code>a</code> to be <code>bytes(1)</code>, but it is <code>b''</code>.
How can I read the contents of the file before truncating it?


A:

You can't. The file was truncated, so of course the contents are gone.
You can, however, use <code>mmap.mmap.read()</code> to read the contents of the file before truncating it.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m.read()
    f.truncate()
</code>

