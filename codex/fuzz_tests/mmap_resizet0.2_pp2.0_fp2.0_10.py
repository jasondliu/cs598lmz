import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that this is because the file has been truncated, but I don't understand why the <code>mmap</code> object is not updated.
Is there a way to update the <code>mmap</code> object?


A:

<blockquote>
<p>Is there a way to update the mmap object?</p>
</blockquote>
No.
<blockquote>
<p>I understand that this is because the file has been truncated, but I don't understand why the mmap object is not updated.</p>
</blockquote>
The <code>mmap</code> object is a view into the file.  It is not a copy of the file.  If you truncate the file, the <code>mmap</code> object is still a view into the file, but the file is now smaller.  The <code>mmap</code> object is not updated because it is not a copy of the file.
<blockquote>
<p>I don't understand why the
