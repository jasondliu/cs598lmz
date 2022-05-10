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

The problem is that you are using <code>mmap.mmap</code> with the <code>length</code> argument set to <code>0</code>. This means that the <code>mmap</code> object will have a length of <code>0</code> bytes.
When you then try to access the <code>mmap</code> object with <code>m[:]</code>, you are trying to access the entire <code>mmap</code> object, which is <code>0</code> bytes long. This is why you get the error.
If you change the <code>mmap</code> call to:
<code>m = mmap.mmap(f.fileno(),
