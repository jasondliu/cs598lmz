import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I'm not sure why I get this error. I'm using Python 3.5.2 on Windows 10.


A:

From the documentation:
<blockquote>
<p>When the file is opened for reading and writing, the file size cannot
  be changed. If the file is opened for writing only, the file size is
  truncated to zero bytes.</p>
</blockquote>
This means that you cannot open the file for reading and writing and then truncate it. You have to open it for writing only.

