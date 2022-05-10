import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the mmap offset is greater than the file size.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that <code>mmap</code> is not updated when you truncate the file.
<code>mmap</code> is a wrapper around the <code>mmap</code> system call, which is documented as follows:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> system call causes the pages starting at <code>&lt;code&gt;addr&lt;/code&gt;</code> and continuing for at least <code>&lt;code&gt;len&lt;/code&gt;</code>
