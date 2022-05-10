import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm using Python 3.6.1 on Windows 10.
I'm trying to understand why this happens. I thought that the mmap object would be aware of the file size change, but apparently it's not.
Is there a way to make the mmap object aware of the file size change?


A:

The <code>mmap</code> object is not aware of the file size change because it is not supposed to be.
The <code>mmap</code> object is a view of the file at a given point in time. It is not a live view of the file.
If you want to truncate the file, you need to unmap the file first.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()

