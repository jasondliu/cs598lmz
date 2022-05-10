import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
Is there any way to update the mapping so that it knows the file was truncated?

I'm using Python 3.5.2 on Windows 10.


A:

I think the problem is that you are using <code>mmap</code> in read-only mode.
When you create the <code>mmap</code> object, you pass <code>0</code> as the size. This means the entire file will be mapped (even if it grows later). However, if you pass <code>0</code>, then the <code>mmap</code> object will be in read-only mode.
If you pass a positive number, then the <code>mmap</code> object will be in read-write mode. In that case, it will be resized automatically when the file is truncated.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap
