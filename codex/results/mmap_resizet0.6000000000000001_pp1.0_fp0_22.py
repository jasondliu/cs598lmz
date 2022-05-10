import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This results in a <code>ValueError</code> as the mmap is backed by the file and the file is changed with <code>truncate()</code>.
A more complicated example:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.write(bytes(1))
    f.write(bytes(1))
    f.truncate()
    f.write(bytes(1))
    a = m[:]
    print(a)
</code>
This results in a <code>mmap.error: [Errno 9] Bad file descriptor</code> as the mmap is backed by the file and the file is changed with <code>truncate()</code>.
Is there a way to have a <code>mmap</code> object that is backed by a file and allows to change the file? If not, is there
