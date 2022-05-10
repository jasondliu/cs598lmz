import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.write(bytes(2))

with open('test', 'rb') as f:
    print(f.read())
</code>
Output:
<code>b'\x01\x02\x00'
</code>
Why does the file only contain 3 bytes?
I am using Python 3.8.1 on Ubuntu 18.04.


A:

From the docs:
<blockquote>
<p>It is important to flush the contents of the file to disk before closing the file. This can be done with the flush() method or by closing the file.</p>
</blockquote>
So when you close the file, the actual size of the file is set to the current position of the file descriptor.
The solution is to call <code>m.flush()</code> before closing the file.

