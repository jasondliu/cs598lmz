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
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand why this happens, but I don't understand why it happens.
The file is opened in <code>r+b</code> mode, so the file pointer is at the beginning of the file.
The <code>mmap</code> object is created with the file descriptor, so it should be aware of the file pointer.
The file is truncated, so the file pointer is still at the beginning of the file.
The <code>mmap</code> object is created with a length of 0, so it should be aware of the file size.
The <code>mmap</code> object is created with an offset of 0, so it should be aware of the file pointer.
So why does it throw an exception?


A:

<blockquote>
<p>The <code>&lt;code&gt;mmap&lt;
