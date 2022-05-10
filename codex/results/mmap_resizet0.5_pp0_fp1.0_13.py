import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises a <code>ValueError</code> with the message <code>mmap length is zero</code>.
What is the correct way to use <code>mmap</code> when the file is truncated?


A:

If you want to change the size of the file, you'll have to unmap it first:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()
    f.truncate()
</code>

