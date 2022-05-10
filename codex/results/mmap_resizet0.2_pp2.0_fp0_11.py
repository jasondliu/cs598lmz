import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws <code>ValueError: mmap offset is greater than file size</code>.
I don't understand why the mmap is not updated when the file is truncated.
I'm using Python 3.5.2 on Windows 10.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>If <em>length</em> is omitted, the current size of the file is used.</p>
</blockquote>
So, you're telling <code>mmap</code> to map the entire file, which is 1 byte long. Then you truncate the file to 0 bytes. The <code>mmap</code> is still 1 byte long, but the file is 0 bytes long.
You can fix this by passing <code>0</code> as the length argument to <code>mmap</code>:
<code>m = mmap.mmap(f.fileno(), 0)
</code>

