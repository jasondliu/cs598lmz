import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect the last line to raise an exception, but it doesn't. It seems <code>mmap</code> retains a reference to the file even after I close it. Does anyone know what is going on here?


A:

<code>mmap</code> is a built-in module, so it is implemented in C and the Python docs for it don't give us any information about its implementation details.  It could be doing anything under the hood.  If you want to find out what it is really doing, you'll have to look at the CPython source code.  You can browse it here: http://hg.python.org/cpython/file/tip/Modules/_mmapmodule.c
I haven't looked at the source code, but I'm guessing that <code>mmap</code> gets something like a file handle from the low level operating system calls, and then uses that to get the file contents.  It's not likely that <code>mmap</code> is actually holding a reference to the Python file object.
Another possibility is that, because the file is opened in <code>r+b</code> mode,
