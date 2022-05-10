import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I was expecting the <code>mmap</code> object to be updated to reflect the new file size. Is there a way to do this?


A:

From the docs:
<blockquote>
<p>If the file is resized, the size of the mmap will not change.</p>
</blockquote>

