import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
It prints <code>b'\x01'</code>, but I expect it to print <code>b''</code>.
I know that the file is truncated, because if I open it with a hex editor, it shows no data.
I also know that the file is truncated, because if I do <code>m.size()</code> it returns <code>0</code>.
I also know that the file is truncated, because if I do <code>m.resize(1)</code> it returns <code>1</code>.
I also know that the file is truncated, because if I do <code>m.read(1)</code> it returns <code>b''</code>.
Why does <code>m[:]</code> return <code>b'\x01'</code>?


A:

The <code>mmap</code> object is not updated when the underlying file is truncated.
The documentation says:
<blockquote>
<p>The mmap object is not updated if the underlying file is changed by other means, e.
