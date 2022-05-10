import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
But in this case <code>a</code> is <code>None</code>, even if the file is opened with <code>r+b</code> and the <code>mmap</code> object is not closed.

EDIT
I need to pass the file handle to another object that expects a file.


A:

A <code>mmap</code> object can be created on top of an open file descriptor, which is what the <code>fileno()</code> method returns.
You don't need to make a copy of the file to do what you want here.
<code>with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>
Keep in mind that the <code>mmap</code> object holds a reference to the underlying file object, which will not be closed until the <code>mmap</code> object is closed.
The documentation describes how to do this:
<blockquote>
<p>To create a named temporary file
