import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
But this is not a good solution. I try to avoid any exceptions.


A:

The file is not being deleted, it's merely being truncated:
<code>&gt;&gt;&gt; import mmap
&gt;&gt;&gt; with open('test', 'wb') as f:
...     f.write(bytes('1'))
...
&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     m.seek(0)
...     m.write(bytes('2'))
...     m.close()
...
&gt;&gt;&gt; with open('test', 'rb') as f:
...     f.seek(0)
...     print(f.read())
...
b'2'
&gt;&gt;&gt;
</code>
It might not be what you want, but it is what you're asking for.
If you want to delete the file, then
