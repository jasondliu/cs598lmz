import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap closed or invalid
</code>
I'm not sure what I'm doing wrong. I'm using Python 3.6.1 on Windows 10.


A:

The problem is that you're trying to use the <code>mmap</code> object after you've truncated the file.  The <code>mmap</code> object is still pointing to the original file size, which is no longer valid.
If you want to truncate the file, you need to do it before you create the <code>mmap</code> object.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
   
