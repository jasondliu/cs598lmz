import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
</code>
This works fine. However, if I try to open the file in append mode, it fails:
<code>with open('test', 'ab') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
</code>
The error message is:
<code>Traceback (most recent call last):
  File "test.py", line 5, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: cannot mmap an empty file
</code>
It seems that <code>mmap.mmap</code> requires the file to be opened in read/write mode. Is there any way around this?


A:

In append mode, the file pointer is at the end of the file. You need to seek to the beginning of the file before you can use <code>mmap</code>.
<code>with open('test', 'ab') as f:
    f.seek(0)
    m =
