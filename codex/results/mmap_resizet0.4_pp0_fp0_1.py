import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code will throw an exception <code>ValueError: mmap offset is greater than file size</code>.
I have a few questions about this:

Why does this happen?
Why does <code>m[:]</code> work at all?
How can I get the data from the file?



A:

<blockquote>
<p>Why does this happen?</p>
</blockquote>
The mmap object is created with a size of 1 byte.  When you truncate the file, the mmap object is still pointing at the same byte of memory, but it's in the middle of nowhere.  When you try to access the byte, it throws an exception.
<blockquote>
<p>Why does m[:] work at all?</p>
</blockquote>
It doesn't.  It throws an exception.
<blockquote>
<p>How can I get the data from the file?</p>
</blockquote>
You can't.  You truncated it.  The data is gone.

