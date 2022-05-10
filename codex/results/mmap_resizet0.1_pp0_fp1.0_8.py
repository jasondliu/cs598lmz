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
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that the file size is 0, but I don't understand why the offset is greater than the file size. I thought that the offset was the position of the file pointer.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that you are using <code>mmap.mmap</code> with the <code>length</code> parameter set to 0. This means that the mmap object will be created with a length of 0, and the offset will be set to the current file position.
When you truncate the file, the file position is not changed, so the offset is still at the end of the file.
If you want to truncate the file and then map it, you need to use <code>mmap.mmap</code> with the <code>length</code> parameter set to the new file size
