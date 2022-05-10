import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get an error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file is truncated and the mmap is not aware of it.
Is there a way to make the mmap aware of the truncation?
I could close the file and reopen it, but I would like to avoid it.


A:

The <code>mmap</code> module is not aware of the file size, it's a view of the underlying file descriptor. 
The <code>mmap</code> object is not aware of the file size, it's a view of the underlying file descriptor. 
The <code>mmap</code> object is not aware of the file size, it's a view of the underlying file descriptor. 
The <code>mmap</code> object is not aware of the file size, it's a view of the underlying file descriptor. 
The <code>mmap</code> object is not
