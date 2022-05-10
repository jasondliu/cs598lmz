import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In this case, it raises <code>ValueError: mmap offset is greater than file size</code>.
I guess the reason is that the <code>mmap</code> object has a reference to the file, and the file is truncated, so the <code>mmap</code> object is invalid.
But I don't know how to solve this problem.
I want to truncate the file, and then read the content of the file.
Any idea?


A:

<code>mmap</code> objects are not designed to be used after the underlying file has been truncated.  The <code>mmap</code> object is a view of the file's contents at a particular point in time.  If the file is truncated, the <code>mmap</code> object is no longer a valid view of the file's contents.
If you want to truncate the file and then read the new contents, you'll have to create a new <code>mmap</code> object.  For example:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap
