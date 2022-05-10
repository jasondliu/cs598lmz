import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print(a)
</code>
This gives me the error:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm not sure why this is happening.  I'm using Python 3.6.3, if that matters.


A:

The problem is that the size of the file has changed, but the mapping is still referring to the old file size.  As a result, you are trying to access data beyond the end of the file, which is not allowed.
You need to use the <code>mmap.resize</code> method to change the size of the mapping.  In this case, you can just set the size to 0.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
   
