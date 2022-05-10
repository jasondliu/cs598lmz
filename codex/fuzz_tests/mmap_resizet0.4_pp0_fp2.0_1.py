import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
I expected the output to be <code>b'\x01'</code>, but instead I got <code>b''</code>.
Why is that?


A:

The <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>Changes made to the mmap object are reflected in the file, and changes made to the file are reflected in the mmap object.</p>
</blockquote>
It does not say that the <code>mmap</code> object is updated when the file is changed outside the <code>mmap</code> object.

