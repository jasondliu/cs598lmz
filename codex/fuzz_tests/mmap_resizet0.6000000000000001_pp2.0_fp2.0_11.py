import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
I would expect <code>a</code> to be empty, but it is <code>b'\x00'</code>.
I have tried this with Python 2.7 and Python 3.5. The same result.
Is there any way to force the mmap to stay up-to-date?


A:

The file is truncated, but the mmap is still active. The mmap isn't reloaded from file until you either close it or do something to it. 
To force it to reload, you need to either unmap it, or just ask it to do something. <code>m.seek(0)</code> will do the trick:
<code>&gt;&gt;&gt; import mmap
&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     f.truncate()
...     print(m.read(1))
...     m.seek(0)
...     print(m
