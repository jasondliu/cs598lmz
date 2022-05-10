import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'1234')
m.close()
</code>
When I use a different <code>test</code> file, it works. If I change <code>r+b</code> to <code>w+b</code>, it works. I'm on Windows 10 and running Python 3.5.2.


A:

from the <code>mmap</code> docs:
<blockquote>
<p>write (bool(1) or bool(0)) If a bool(0) or bool(0) is specified, a read-only mapping is ensured (an exception is thrown if that’s not possible), otherwise a read-write mapping is requested.</p>
</blockquote>
so only passing read as <code>prot</code> works for me:
<code>from mmap import ACCESS_WRITE, mmap

f = open('foo.txt', 'r+')
m = mmap(f.fileno(), 0, access=ACCESS_WRITE)
m.seek(0)  # rewind
m.write(b'data')

