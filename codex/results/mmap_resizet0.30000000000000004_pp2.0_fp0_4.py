import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code> exception.
I've tried to use <code>m.resize()</code> and <code>m.close()</code> methods, but it doesn't help.
Is there any way to avoid this exception?


A:

You can't use <code>mmap</code> to read from a file that has been truncated. 
<code>mmap</code> is a view into a file. When you truncate the file, the view is no longer valid.
If you want to read from a file that has been truncated, you'll have to read from the file itself, not from the <code>mmap</code> object.

