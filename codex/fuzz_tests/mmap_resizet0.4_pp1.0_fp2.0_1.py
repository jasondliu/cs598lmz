import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
It prints <code>b'\x01'</code> which is the byte I wrote.
But if I change the file to <code>'r+t'</code> it prints <code>b''</code> (empty byte).
I don't understand why the <code>mmap</code> object is not updated when the file is truncated.


A:

<blockquote>
<p>I don't understand why the mmap object is not updated when the file is truncated.</p>
</blockquote>
The <code>mmap</code> object is updated.  The <code>bytes</code> object you create from the <code>mmap</code> object is not updated.
<code>a = m[:]
</code>
creates a new <code>bytes</code> object from the <code>mmap</code> object.  That <code>bytes</code> object is not updated when the <code>mmap</code> object is updated.  It is a snapshot of the <code>mmap</code> object at the time
