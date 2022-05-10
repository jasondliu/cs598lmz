import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code will give you an error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 3, in &lt;module&gt;
TypeError: object of type '_io.BufferedRandom' has no len()
</code>
But this one does not:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I know that this problem is related to the fact that the <code>m</code> variable represents the file in memory and the <code>f</code> variable represents it on disk, and that the <code>m[:]</code> is just some kind of 'caching' of the file on disk. I also know that I can solve this problem by just replacing <code>m</code> with
