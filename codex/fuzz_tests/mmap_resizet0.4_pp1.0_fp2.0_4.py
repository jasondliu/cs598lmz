import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be <code>b'\x01'</code>, but instead it is <code>b''</code>.
Why does this happen? How can I achieve the expected result?


A:

When you truncate the file, the mmap object becomes invalid.
<blockquote>
<p>When the file is closed or the object is garbage-collected, the underlying file is closed, and any changes to the file contents or size are written to disk.</p>
</blockquote>
You can try to create a new mmap object after the truncate, but it will start at the beginning of the file, so you'll need to seek to the end to get the byte you want.

