import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<code>a</code> is <code>b'\x00'</code> instead of <code>b'\x01'</code>.
<code>m</code> is still valid.
<code>m[:]</code> is <code>b'\x01'</code>.
<code>m.size()</code> is <code>0</code>.
<code>m.tell()</code> is <code>0</code>.
<code>m.seek(0)</code> does nothing.
<code>m.seek(0, 1)</code> does nothing.
<code>m.seek(0, 2)</code> does nothing.
<code>m.flush()</code> does nothing.
<code>m.close()</code> does nothing.
<code>m.resize(1)</code> does nothing.
<code>m.resize(0)</code> does nothing.
<code>m.move(0, 0, 0)</code> does nothing.
<code>m.move(0, 1, 0)</code>
