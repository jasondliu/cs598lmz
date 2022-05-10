import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>


A:

If you want to truncate the file, you must use the <code>length</code> parameter of <code>mmap.mmap()</code> to specify the new size.
If you don't, the mmap object will see the original file size, not the truncated one.
<code>with open('test', 'w') as f:
    f.write('hello')
with open('test', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate(2)
    print repr(m[:])
</code>
outputs
<code>'he'
</code>

