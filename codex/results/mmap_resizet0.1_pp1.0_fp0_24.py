import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expect the output to be <code>b'\x01'</code>, but it is <code>b''</code>.
I know that I can use <code>m.resize(0)</code> to truncate the file, but I want to know why the above code doesn't work.


A:

The <code>mmap</code> object is not updated when the file is truncated.
The documentation says:
<blockquote>
<p>The mmap object is not updated if the file is changed by another process after the mmap is created.</p>
</blockquote>

