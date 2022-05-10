import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line raises <code>ValueError: mmap closed or invalid</code>.
I've tried to use <code>mmap.resize</code> to resize the map, but it doesn't work either.
Is there a way to resize the map?


A:

You can't resize a map in-place. You need to create a new map, and then copy the data over.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m2 = mmap.mmap(f.fileno(), 0)
    m2[:] = m[:]
    m.close()
    m2.close()
</code>

