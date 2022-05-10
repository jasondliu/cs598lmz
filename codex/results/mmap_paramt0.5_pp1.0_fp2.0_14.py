import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
</code>
The file is created and it's size is 2 bytes.
However, when I try to write the same thing to a memory mapped file of a file that doesn't exist, I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m = mmap.mmap(-1, 0)
ValueError: mmap length is zero
</code>
What is the reason for this? Is there a way to create a memory mapped file that doesn't have a corresponding file on disk?


A:

You have to specify a file descriptor, not a file name.
For example:
<code>import mmap

fd = os.open('test', os.O_RDWR|os.O_CREAT)
m = mmap.mmap(fd, 0)
</code>
From the docs:
<blockquote>
<p>The constructor creates a memory-mapped file object for the specified file descriptor fd. The size argument specifies the initial size of
