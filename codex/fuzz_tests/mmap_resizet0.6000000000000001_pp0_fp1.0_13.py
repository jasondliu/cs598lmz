import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line throws a <code>ValueError</code>:
<code>ValueError: mmap offset is greater than file size
</code>
But the mmap offset is 0.
This is python 2.7.11, 64bit, windows.
Is this the expected behaviour?


A:

The problem is that you are calling <code>f.truncate</code> after creating the <code>mmap</code> object and before accessing the <code>mmap</code> object.
<code>mmap</code> objects keep track of the current file size, and when you truncate the file, the <code>mmap</code> object is still trying to access the old file size. This is why you are getting the exception.
If you switch the order of those two statements, you will not get the exception:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    a = mmap.mmap(f.fileno
