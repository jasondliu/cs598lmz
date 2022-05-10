import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect <code>a</code> to be <code>b'\x01'</code>, but instead it is <code>b''</code>.
What is the problem here?


A:

The problem is that the <code>mmap</code> object is not "resized" when you truncate the file.
You can see this with:
<code>&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     f.truncate()
...     print(m.size())
...     a = m[:]
... 
1
</code>
You can resize the <code>mmap</code> object manually:
<code>&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     f.truncate()
...     m.resize(0)
...     print(m.size())
...
