import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x01'</code>.
I thought that the mmap object would be invalidated after the call to <code>truncate()</code>. Is this not the case?


A:

The docs for <code>mmap</code> state (under "Windows support"):
<blockquote>
<p>On Windows, files are always mapped in copy-on-write mode.</p>
</blockquote>
So the <code>mmap</code> object only becomes invalid after you write to it.

