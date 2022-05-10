import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
    m.flush()

with open('test', 'rb') as f:
    print(f.read())
</code>
The result is <code>b'\x02'</code>, which is expected.
However, if I remove <code>m.flush()</code> the result is <code>b'\x01'</code> instead of <code>b'\x02'</code>.
What is the reason for that?


A:

It's because, as the documentation for <code>mmap</code> states:
<blockquote>
<p>All modifications to a memory map are automatically committed to the underlying file.</p>
</blockquote>
(Emphasis added.)
If you want to avoid that, you can use <code>mmap.MAP_PRIVATE</code> instead of <code>mmap.MAP_SHARED</code>.

