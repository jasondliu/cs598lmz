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
I don't understand why this happens. The file is open and the mmap object is still valid.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that the <code>mmap</code> object is still pointing to the old file size.
<code>mmap.mmap</code> takes a <code>length</code> argument, which defaults to the size of the file. You are passing in <code>0</code>, which means "the size of the file".
When you truncate the file, the <code>mmap</code> object is still pointing to the old file size.
You can fix this by passing in the new file size:
<code>with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mm
