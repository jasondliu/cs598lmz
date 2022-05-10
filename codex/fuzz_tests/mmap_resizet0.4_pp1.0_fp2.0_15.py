import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap closed or invalid
</code>
I don't understand why the <code>mmap</code> is closed. I didn't close it explicitly.
If I remove the line <code>f.truncate()</code>, the code works.
I'm using Python 3.5.2 on Windows 10.


A:

The problem is that the <code>mmap</code> object is tied to the underlying file, and when you truncate it, the <code>mmap</code> object is no longer valid.
From the documentation:
<blockquote>
<p>When a file is opened for updating, the <code>&lt;code&gt;mmap&lt;/code&gt;</code> object can be used to read and write data in the file. If the file is resized, the <code>&lt;code&gt;
