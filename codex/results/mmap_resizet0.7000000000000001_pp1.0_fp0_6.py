import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It's not a simple question and I don't know, where the problem is.
I've got a following error:
<blockquote>
<p>Traceback (most recent call last):</p>
<p>File "C:/Users/mb/PycharmProjects/test/test.py", line 7, in </p>
<p>a = m[:]</p>
<p>ValueError: memory view cannot include disjoint buffers</p>
</blockquote>


A:

If a file is truncated while the mmap exists, that is a disaster.  The mmap is backed by that file and the data it contains, and if the file is truncated, the mmap no longer has the same data it did.
Remember that mmap is just a memory mapping of a file.  Truncating a file is like cutting off a part of a memory object.  It just doesn't make sense.  If a file is truncated, there is no real way to resize the mmap to match the new size of the file.
This is why it is recommended that you not truncate a file that
