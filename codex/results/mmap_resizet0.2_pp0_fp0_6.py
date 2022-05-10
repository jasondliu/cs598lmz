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
ValueError: mmap offset is greater than file size
</code>
I am using Python 3.6.1 on Windows 10.
I am trying to understand how to use <code>mmap</code> to read and write to a file. I am trying to understand how to use <code>mmap</code> to read and write to a file. I am trying to understand how to use <code>mmap</code> to read and write to a file. I am trying to understand how to use <code>mmap</code> to read and write to a file. I am trying to understand how to use <code>mmap</code> to read and write to a file. I am trying to understand how to use <code>mmap</code> to read and write to a file. I am trying to understand how to use <code>mmap</code> to read and write to a file. I
