import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
this fails because <code>f.truncate()</code> unlinks the file object from <code>m</code>.
What I want is that <code>f.truncate()</code> will raise a <code>WindowError</code>, because otherwise the reference to <code>m</code> is useless.
The only way I can see to make <code>f.truncate()</code> to raise <code>WindowError</code> is to use <code>mmap.MAP_SHARED</code> flag, which is not what I want.
Is there any way to make truncate to raise <code>WindowError</code>?
EDIT:
I want the following behavior:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(hex(f.tell()))
    m.seek(5)
