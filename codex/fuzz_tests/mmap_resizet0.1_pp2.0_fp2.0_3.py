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
I would expect the <code>mmap</code> to be updated when the file is truncated.
I am using Python 3.6.4 on Windows 10.


A:

The problem is that you are using <code>mmap.mmap</code> with the <code>length</code> parameter set to 0. This means that the <code>mmap</code> object will be mapped to the entire file.
When you truncate the file, the <code>mmap</code> object is still mapped to the entire file, but the file is now empty.
You can fix this by setting the <code>length</code> parameter to the size of the file before you truncate it.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(
