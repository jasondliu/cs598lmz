import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the error:
<code>ValueError: mmap can't resize a read-only or copy-on-write (COW) file
</code>
I don't understand why this is happening. I'm not even resizing the file. I'm just trying to read from it. I also don't understand why the error message is saying that the file is copy-on-write. I'm not even trying to modify the file.
Thanks.


A:

You can't read from a <code>mmap</code> object after the file has been truncated.
From the docs:
<blockquote>
<p>If the file is resized smaller, the extra data in the mmap object is discarded. If the file is resized larger, the extra space is readable and writable, and corresponds to the contents of the underlying file.</p>
</blockquote>
The file has been resized smaller, so the extra data in the <code>mmap</code> object has been discarded.

