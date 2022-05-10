import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
This works fine, but it has a couple of problems:

It's not obvious that the file needs to be opened in binary mode.
It's not obvious that the file needs to be opened in read/write mode.

Is there a way to do this without opening the file in read/write mode?


A:

You can open the file in read-only mode and use <code>mmap.ACCESS_WRITE</code> as the access mode:
<code>&gt;&gt;&gt; with open('test', 'rb') as f:
...     m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
...     m[0] = bytes(2)
...     m.close()
...
&gt;&gt;&gt; with open('test', 'rb') as f:
...     print(f.read())
...
b'\x02'
</code>

