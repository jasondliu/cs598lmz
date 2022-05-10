import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # pointer to what was there
    try:
        m[:] = bytes(2)
    except Exception as e:
        print(type(e))
    f.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m[:] = bytes(2)
</code>
Output:
<code>&lt;class 'ValueError'&gt;
</code>


A:

This happens because <code>mmap.mmap()</code> takes a length as the second argument. It creates a mapping for that number of bytes, beginning at the start of the file.
When you truncate the file, <code>m[:] = bytes(2)</code> won't work anymore since the mapping is no longer valid.
You can use the <code>mmap.ACCESS_WRITE</code> access mode to allow the mapping to be resized (fixed in 3.3+):
<code>m = mmap.mmap(f.fileno(), 0, access=mm
