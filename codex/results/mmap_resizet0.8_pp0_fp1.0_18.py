import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
If I remove <code>f.truncate()</code>, the error is not raised.
The documentation says that <code>mmap.mmap(file_obj, length, tagname=None, access=ACCESS_DEFAULT, offset=0)</code> should provide "a memory-map to an array of length bytes backed by the given file". 
So, I expected the memory to be acessible in both ways, <code>f.read()</code> and <code>m[:]</code>.
I'm using Python 3.5.2


A:

I found the answer here: https://mail.python.org/pipermail/python-list/2012-March/623822.html
After truncating the file, the <code>mmap</code> object is still valid, but the length is not updated. So the object continues to point to the previous size of the file.

