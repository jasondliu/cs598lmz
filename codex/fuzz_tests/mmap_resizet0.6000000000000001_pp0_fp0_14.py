import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I would expect this to throw an exception, but it prints <code>b'\x01'</code>, which is the first byte of the file.
This is on Windows 10, Python 3.5.2, but I've also seen it on Linux, Python 3.5.1.
So, is this a bug in Python, or in my understanding of how mmap is supposed to work?
EDIT: I've opened an issue on the Python bug tracker.


A:

It looks like this is a bug in Python.
From the documentation for <code>mmap</code>:
<blockquote>
<p>If the file is resized by another process, the mmap object behaves as if the new data were present all along (but the old data disappears).</p>
<p>If the file is resized by another process, the mmap object behaves as if the new data were present all along (but the old data disappears).</p>
</blockquote>
So, since the file was resized by the same process, I would expect the same behavior.

