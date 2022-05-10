import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I was expecting <code>a</code> to be <code>b''</code> but instead I got <code>b'\x01'</code>
If I instead initialize the mmap with <code>mmap.ACCESS_WRITE</code> it works as expected.
I don't get this behavior if I <code>open('test', 'rb+')</code> instead of <code>open('test', 'r+b')</code>
What does <code>open('test', 'r+b')</code> do that is causing this behavior?


A:

This is a known bug in the standard library:

https://bugs.python.org/issue27556


In short, it's a bug in the library. 
The underlying problem is that <code>io.FileIO</code> doesn't update its internal file pointer when you truncate the file. 
It works in most cases, because the file pointer is at the end of the file, and thus identical to the <code>end</code> parameter. So <code>acc.read()</code> returns <code>
