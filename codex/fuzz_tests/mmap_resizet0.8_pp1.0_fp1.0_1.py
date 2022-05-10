import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last statement raises <code>ValueError: mmap offset is beyond the end of the file</code>.
But the following does not raise this error:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    f.truncate()
    a = m[:]
</code>
Why does the <code>mmap</code> object allow accessing beyond the end of the file in the second case but not the first? I understand the reference to offset being beyond the end of the file in the error, but in both cases the offset is 0.


A:

From the documentation:
<blockquote>
<p>mmap(fileno, length[, tagname[, access[, offset]]])</p>
<p>Return a <em>memory-map</em> object for the file specified by the file handle fileno. The length argument specifies the number of bytes to map. tagname
