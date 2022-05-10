import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I expected <code>a</code> to be an empty byte string.
Why is this happening?


A:

The <code>mmap</code> object is still pointing to the same location in the file, even though you've truncated the file.
You can see this by printing the <code>mmap</code> object:
<code>&gt;&gt;&gt; print(m)
&lt;mmap.mmap object at 0x7f9b7d46b8c0&gt;
</code>
The <code>mmap</code> object is just a wrapper around a memory-mapped file.  It doesn't care about the file size.  It just points to a location in the file.  If you truncate the file, it's still pointing to the same location.  The file is smaller, so it's pointing to a location that's no longer in the file.
If you want to use the <code>mmap</code> object, you'll have to <code
