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
I understand that the file size is 0, but I don't understand why the mmap offset is greater than the file size. 
I'm using python 3.5.2 on Ubuntu 16.04.


A:

The <code>mmap</code> offset is the offset in the file. You truncated the file to 0 bytes, so the offset is now past the end of the file.
You can't truncate a file that has an open <code>mmap</code> object. You'll have to <code>close()</code> the <code>mmap</code> object first, then truncate the file, then reopen the file and create a new <code>mmap</code> object.

