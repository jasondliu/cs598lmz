import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # ERROR: m.getline()
</code>
I'm trying to replace the <code>m.getline()</code> with something more appropriate, but I'm not sure what.
I'm aware of the <code>mmap.resize</code> method, but I don't want to change the size of the <code>mmap</code> object, just its file. 

