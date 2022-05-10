import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I am trying to truncate the file and then read the bytes using <code>mmap</code> but I am getting <code>ValueError: cannot mmap an empty file</code>. I did some research on this and got to know that <code>mmap</code> does not work on empty file. Is there any way to read the contents of the file after truncating it using <code>mmap</code>?


A:

You have to unmap the file before you truncate it:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()
    f.truncate()
</code>

