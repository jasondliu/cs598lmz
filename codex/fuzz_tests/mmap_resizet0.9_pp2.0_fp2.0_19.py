import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the error:
mmap.error: [Errno 22] Invalid argument


A:

The <code>mmap</code> read raises an exception because there is nothing left to read.
The <code>mmap</code> _mmap instance was created using <code>MMAP_PRIVATE</code> - this creates a private copy of the original file, so any changes made to the <code>mmap</code> won't be written to disk.  When <code>truncate()</code> is called it only changes the <code>FILE</code> on disk, not the copy in the <code>mmap</code>.
You can use
<code>m.resize(0)
</code>
This will then cause <code>read()</code> to return <code>''</code>
Example
<code>from mmap import mmap, ACCESS_COPY, PROT_READ

with open('test', 'r+b') as f:
    m = mmap(f.fileno(), 0, access=ACCESS_COPY)

