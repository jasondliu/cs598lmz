import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises a <code>ValueError</code> with the message <code>mmap offset is greater than file size</code>.
I understand that the file has been truncated, but I don't understand why the <code>mmap</code> object is still trying to access the file.
What is the correct way to truncate a file with a <code>mmap</code> object?


A:

You can't do this.  The <code>mmap</code> object is a view into a file, and it can't be changed to refer to a different file.  You can't even change the file size while the <code>mmap</code> object is in use.
You have to close the <code>mmap</code> object before you truncate the file.

