import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line throws a <code>ValueError: mmap closed or invalid</code> exception. I'm guessing this is because the size of the file has been changed.
Is there a way to get around this?
Note that I don't want to use the <code>access=mmap.ACCESS_READ</code> argument because I want to be able to write to the mapped area.

