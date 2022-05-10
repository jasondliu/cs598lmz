import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that <code>mmap</code> is not aware of the truncation, but is there a way to make it aware?
I'm using Python 3.6.


A:

The documentation for <code>mmap.mmap</code> says:
<blockquote>
<p>If <em>length</em> is larger than the current size of the file, the file is extended to contain <em>length</em> bytes. If <em>length</em> is 0, the maximum length of the map is the current size of the file, except that if the file is empty the map must be zero-filled, so an empty but writeable file must have a length of at least one byte.</p>
</blockquote>
So, if you want to be able to read the entire file, you need to specify a length of at least 1.

