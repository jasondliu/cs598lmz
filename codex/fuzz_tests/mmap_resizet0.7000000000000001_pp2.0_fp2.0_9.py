import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
For the first time it will print <code>(1, )</code>, but for all the next times I get <code>(0, )</code>.
I'm sure this is not a Python bug, so what am I doing wrong?


A:

The documentation is clear that the data is no longer valid after the truncate:
<blockquote>
<p>After the file is resized, any references to bytes beyond the new size are invalid, and may cause errors if the memory is accessed.</p>
</blockquote>
A <code>mmap</code> object is a view of the file, and its view of the file is no longer valid after the file is resized.
If you want to keep the data, you need to write it to a new file before truncating the original one.

