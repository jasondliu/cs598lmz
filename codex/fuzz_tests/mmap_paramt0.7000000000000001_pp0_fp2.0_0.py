import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, None, mmap.ACCESS_WRITE)
    m.write(bytes(2))
</code>
This gives an <code>OSError: [Errno 22] Invalid argument</code>
According to the docs, <code>mmap.ACCESS_WRITE</code> is supposed to map the file for reading and writing, but it doesn't seem to work.
The docs for <code>mmap.mmap</code> imply that using <code>mmap.ACCESS_COPY</code> would also work, but it doesn't.
What am I doing wrong? Is it even possible to use <code>mmap</code> to read and write a file that is opened in text mode?


A:

You can read and write to a memory-mapped file using it as an array.  The Python documentation on the <code>mmap</code> module gives an example:
<code>&gt;&gt;&gt; m = mmap.mmap(-1, 1024, access=mmap.ACCESS_READ)
&gt;&gt;&gt; m.write('Hello
