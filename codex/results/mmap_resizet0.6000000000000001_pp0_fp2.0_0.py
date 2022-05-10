import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This is the error I get:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I am using Python 3.5.1 on Ubuntu.
Is there any way to keep the file open and not have to reopen it? The <code>truncate</code> method is just an example. I would like to be able to use other file methods without having to reopen the file.


A:

I think the operation you are trying to do is not supported by <code>mmap</code>.
The reason is that <code>mmap</code> is not a Python abstraction, it is a system call.
The documentation of <code>mmap</code> system call says:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> system call causes the pages starting at <code>&lt;code&gt;addr&lt;/code
