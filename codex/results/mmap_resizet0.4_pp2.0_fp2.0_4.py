import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    # m.resize(0)
    m.close()
</code>
This code fails with the following error:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap closed or invalid
</code>
I guess the problem is that I'm trying to read from the mmap object after closing it. But I don't understand why. I'm not closing the mmap object until after I'm done reading from it.
So why does this code fail?


A:

<code>mmap</code> objects have a <code>resize</code> method, which you can use to resize the underlying file.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    m.close()
</code>

