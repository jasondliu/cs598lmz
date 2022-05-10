import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Output:
<code>b'\x00'
</code>
I suppose this means that the memory mapping has been cleared. I can't find any documentation to confirm this. Is this intended behaviour? If it is, is there a way to insert a variable-length string into the memory-mapped file?


A:

I think the documentation is pretty clear about this.
The <code>truncate</code> documentation says:
<blockquote>
<p>Truncate the file’s size. If the optional size argument is present, the file is truncated to (at most) that size. The size defaults to the current position. The current file position is not changed.</p>
</blockquote>
And <code>mmap</code>'s documentation says:
<blockquote>
<p>The data in a file-backed mmap cannot be changed by normal means. To modify the data, use mmap.write() (to modify a file-backed mmap) or mmap.resize() (to resize a file-backed mmap).</p>
</blockquote
