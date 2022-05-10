import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I think the reason is that <code>f.truncate()</code> makes the file size 0, but the offset of the mmap is still 1.
Is there a way to make the mmap offset 0?


A:

You can't.
The <code>mmap</code> object is a view of the file, and the file is truncated.
You can't change the view to be a view of the truncated file.
You can create a new <code>mmap</code> object, but you can't change the existing one.

