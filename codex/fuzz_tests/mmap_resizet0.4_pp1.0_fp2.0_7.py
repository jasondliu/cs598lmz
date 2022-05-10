import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I think that this is because the <code>mmap</code> object keeps the old file size.
Is there any way to update the <code>mmap</code> object?


A:

<blockquote>
<p>I think that this is because the mmap object keeps the old file size.</p>
</blockquote>
No, it's because the <code>mmap</code> object is still pointing to the old file size.
<blockquote>
<p>Is there any way to update the mmap object?</p>
</blockquote>
No, there isn't.  The <code>mmap</code> object is a view into the file, and it can't be updated.  You can create a new <code>mmap</code> object, but that will be a new view into the file.

