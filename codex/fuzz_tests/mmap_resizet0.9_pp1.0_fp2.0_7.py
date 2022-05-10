import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This snippet raises with <code>ValueError: cannot truncate a mapped file</code> exception. But, if I change <code>mmap.mmap</code> call to 
<code>m = mmap.mmap(f.fileno(), 7)
</code>
It will be ok.
Can somebody explain, why I need to specify size of mmap when I just want to change file length to zerro?

