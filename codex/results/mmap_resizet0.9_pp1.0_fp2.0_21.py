import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This gives <code>ValueError: mmap closed or invalid</code> on OSX (Python 2.7.12). Is this a bug with <code>truncate()</code>, or is it expected behavior, and if so, how do I properly do this? Obviously, as a workaround, I can call <code>m.resize()</code> after truncation, but that's a lot of syscalls, isn't it.
Adding a <code>m.seek(0)</code> before the <code>m[:]</code> doesn't change anything, presumably because the buffer is already invalid.
EDIT: This appears to be a bug in Mac OSX's mmap implementation. I looked through the Python source, and it looks like there are no conditions where after doing a "valid" call to <code>mmap()</code>, calls to <code>truncate()</code> would close the mapped file. I can reproduce this with <code>python3 -m mmap</code>: 
<code>import mmap
m = mmap.mmap(-1, 0)
m.write(b'abc')
