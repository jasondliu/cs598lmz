import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    f.truncate()
</code>
The error is
<code>ValueError: memory view cannot refer to a memory block that was already freed
</code>
Is there any way to do that?
I am running Python 3.5.3 on macOS Sierra 10.12.6

