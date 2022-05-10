import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>
I can't understand why the <code>mmap</code> object still thinks it is mapped to a file of length 1, even though the file has been truncated.
Is there a way to make the <code>mmap</code> object aware that the file has been truncated?


A:

I think the problem is that you are using the <code>mmap.mmap</code> constructor.  If you use the <code>mmap.mmap</code> function, the <code>mmap</code> object will be aware of the truncation.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>

