import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<code>a</code> is empty, but I expected it to be <code>b'\x01'</code>. Why?


A:

A <code>mmap</code> object is a view of the file, and the size of the file is fixed when you create the <code>mmap</code> object. You can use <code>mmap.resize</code> to change the size of the file and the size of the <code>mmap</code> object:
<code>&gt;&gt;&gt; with open('test', 'wb') as f:
...     f.write(bytes(1))
... 
&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     f.truncate()
...     m.resize(0)
... 
&gt;&gt;&gt; with open('test', 'rb') as f:
...     assert f.read() == b''
... 
</code>
