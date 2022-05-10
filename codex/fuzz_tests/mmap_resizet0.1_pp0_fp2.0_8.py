import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Linux, but on Windows it raises <code>ValueError: mmap offset is greater than file size</code>.
I've tried to use <code>m.resize(0)</code> instead of <code>f.truncate()</code>, but it doesn't help.
Is there any way to truncate file on Windows without closing mmap?


A:

I've found the solution.
<code>m.resize(0)</code> doesn't work because it doesn't change file size.
<code>m.resize(1)</code> works, but it's not what I need.
<code>m.resize(0)</code> + <code>m.flush()</code> works.

