import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
    m.close()
</code>
But this fails with <code>TypeError: mmap can't modify a readonly memory map</code>.
I'm using Python 3.6.4.
Is there any way to make this work?


A:

You need to open the file with <code>'rw'</code> (as opposed to <code>'r+'</code>):
<code>with open('test', 'rw') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
    m.close()
</code>
This is because <code>'r+'</code> is a "read/write" mode, not "read/write/execute" mode.

