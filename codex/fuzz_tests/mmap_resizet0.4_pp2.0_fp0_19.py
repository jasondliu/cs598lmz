import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Here, I get an <code>IndexError</code> exception.
I know that I can use <code>mmap.resize</code> to change the size of the mmap object, but I need to change the size of the underlying file as well.
How can I do that?


A:

<code>mmap</code> is a memory-mapped file, which means it maps the file's contents into memory.  It doesn't know anything about the file.  If you truncate the file, the mmap object is still pointing to the same memory, which is no longer mapped to the file.  The <code>IndexError</code> is because you're trying to access memory that is no longer mapped to anything.
If you want to resize the file and the mmap object, you need to do something like this:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.res
