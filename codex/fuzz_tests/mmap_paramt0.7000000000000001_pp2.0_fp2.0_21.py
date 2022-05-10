import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    result = m.read(1)
    print(result)
    m.close()
</code>
Output: b'\x00'
Also, if I use the same code with <code>f = open('test', 'w+b')</code>, the output is <code>b''</code>. What's going on here?


A:

The <code>mmap</code> class has a <code>resize</code> method.  And <code>resize</code> will always insert <code>NUL</code> bytes to fill the new space.
Using the file <code>test</code> created by the posted code:
<code>&gt;&gt;&gt; print(open('test', 'rb').read())
b'\x00'
</code>
This will change the file size to 10 bytes:
<code>&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     m.resize(10)
...
