import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
You'll see that the last line (read), raises <code>ValueError: cannot truncate a read-only memory mapped array</code>.
This is because Python has to emulate a read-only buffer.
In Python 3, the native <code>io</code> module has <code>BufferedReader(BufferedIOBase)</code> and <code>BytesIO</code> (which can be built around a <code>mmap</code>-like array).
In Python 2.x, the <code>mmap</code> module provides a slightly buggy emulation for Python 2.x.
What I'd like to know is:
Why isn't access to the underlying file given?
Is it due to a limitation in Python itself? Or is the underlying C-API not providing the functionality? Can the Python API easily be changed to provide this functionality?


A:

Working with a <code>mmap</code> object is like working with a file; you can write to it, but you can't truncate it.
You can, however, ask the <code>mmap</code> object to change its size with <code>mmap
