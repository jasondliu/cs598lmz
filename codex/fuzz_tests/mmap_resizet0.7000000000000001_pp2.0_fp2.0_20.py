import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Somehow when truncating the file with lines 4-5, the 'a' variable still contains the byte that was previously written to the file. Why is this?


A:

I think you need to <code>seek</code> to the start of the memory map before using it, and <code>flush</code> on the <code>mmap</code> and <code>f</code> before <code>truncate</code>.
<code>&gt;&gt;&gt; with open('test', 'r+b') as f:
...     m = mmap.mmap(f.fileno(), 0)
...     m.seek(0)
...     m.flush()
...     f.flush()
...     f.truncate()
...     a = m[:]
... 
&gt;&gt;&gt; a
b''
</code>

