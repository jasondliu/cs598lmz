import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises an error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I'm confused why the <code>mmap</code> object is not updated when the file is truncated. Is there a way to force the <code>mmap</code> object to be updated after the file is truncated?


A:

I think the problem is that you are trying to change the file size after it has been opened. 
If you try the following, it works:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.seek(0)
    f.truncate()
    a = m[:]
</code>

