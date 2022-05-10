import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line raises <code>ValueError: mmap closed or invalid</code>.
I understand that the file is truncated, but I don't understand why the mmap is invalidated.
I'm using Python 3.6.1 on Windows 10.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>The file size cannot be changed while the file is mapped.</p>
</blockquote>
So, you can't truncate the file while it's mapped.

