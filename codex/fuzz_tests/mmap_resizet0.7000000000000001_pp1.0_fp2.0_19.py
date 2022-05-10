import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
    f.close()
</code>
I'm getting error:
<code>ValueError: mmap closed or invalid
</code>
I have tried to use <code>mmap.ACCESS_READ</code>, but it doesn't work.


A:

From <code>mmap</code> documentation:
<blockquote>
<p>After the file is closed, the underlying mmap object is still usable.</p>
</blockquote>
You should read the file contents before closing the file.

