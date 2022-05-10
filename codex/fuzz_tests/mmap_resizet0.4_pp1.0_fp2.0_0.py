import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws a <code>ValueError: mmap offset is greater than file size</code>.
I would expect the slice to return an empty bytes object.
Is this a bug in Python? Or am I doing something wrong?


A:

The documentation for <code>mmap.mmap</code> states:
<blockquote>
<p>Note that modifications to the underlying file do not change the contents of the mmap object. For example, if you open a file and write to it, the mmap object will not reflect the new data unless you call <code>&lt;code&gt;mmap.mmap.flush()&lt;/code&gt;</code> or <code>&lt;code&gt;mmap.mmap.close()&lt;/code&gt;</code>.</p>
</blockquote>
So the <code>truncate</code> call doesn't affect the <code>mmap</code> object.

