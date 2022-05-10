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
It prints <code>b'\x00'</code>, but I expected <code>b'\x01'</code>. Why?
I'm on Windows 10, Python 3.8.0.


A:

The docstring of <code>mmap.mmap</code> says:
<blockquote>
<p>Changes to the file object will not be reflected in the mmap object, and vice versa.</p>
</blockquote>
You truncated the file after creating the mmap. The mmap will always reflect the file as it was when the mmap was created.

