import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = m[:]
</code>
I get the error:
<code>ValueError: mmap closed or invalid
</code>
I understand that the file is truncated and so the mmap is invalid, but I don't understand why <code>m[:]</code> is being called twice. I would expect that the second call to <code>m[:]</code> would simply return the empty string.


A:

The <code>__getitem__</code> method is called when you index the object. So when you assign the value of <code>m[:]</code> to <code>a</code>, the method is called. The second time it is called when you assign the value of <code>m[:]</code> to <code>b</code>.

