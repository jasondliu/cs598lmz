import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This prints an empty byte array, which is correct.
However, if I open the file for reading only, I get a <code>ValueError</code>:
<code>with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
<blockquote>
<p>ValueError: cannot truncate a read-only memory map</p>
</blockquote>
I thought that if I opened the file for reading, truncating it should be safe, as the map shouldn't be affected.
I'm using Python 3.6.1.


A:

<code>mmap</code> is a way to map the contents of a file into memory. If you truncate the file, it will be truncated in memory as well. If you open the file read-only, the <code>mmap</code> wrapper won't be able to truncate it.

