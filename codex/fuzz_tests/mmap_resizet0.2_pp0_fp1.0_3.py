import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that the problem is that the file is truncated, so the offset is greater than the file size.
But why does <code>mmap</code> not raise an error when I try to access the file?
Is there a way to make <code>mmap</code> raise an error when I try to access the file?


A:

<code>mmap</code> is a wrapper around the <code>mmap</code> system call.  The system call doesn't raise an error when you access the file, so neither does <code>mmap</code>.
The system call is defined to return <code>MAP_FAILED</code> when it fails, which is <code>-1</code> on most systems.  When you try to access the file, you get a <code>TypeError</code> because <code>mmap</code> returns <code>-1</code> instead of a <code>mmap</code> object.

