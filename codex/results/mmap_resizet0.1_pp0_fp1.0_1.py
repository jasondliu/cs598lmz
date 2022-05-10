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
I'm not sure why this is happening. I'm using Python 3.6.1 on Windows 10.


A:

The problem is that you are using <code>mmap.mmap</code> with the <code>length</code> parameter set to <code>0</code>. This means that the <code>mmap</code> object will be created with a length of <code>0</code> bytes.
When you then call <code>f.truncate()</code>, the file is truncated to <code>0</code> bytes. This means that the <code>mmap</code> object is now pointing to a file that is <code>0</code> bytes long.
When you then try to access the <code>mmap</code> object, it tries to read <code>0</code> bytes from the
