import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I think that this is because the file is truncated before the <code>mmap</code> object is created.
Is there a way to avoid this error?
I know that I can use <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code> to avoid this error, but I want to know if there is a way to avoid this error without using <code>mmap.ACCESS_WRITE</code>.


A:

You can't.
The <code>mmap</code> object is a view of the file, and when you truncate the file, the view is no longer valid.
If you want to truncate the file, you need to close the <code>mmap</code> object first.

