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
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I'm not sure why this is happening. I'm using Python 3.6.1 on Windows 10.


A:

The problem is that you're trying to access the <code>mmap</code> object after you've truncated the file.  The <code>mmap</code> object is still pointing to the old file size, which is now zero.
If you move the <code>truncate</code> call to before the <code>mmap</code> call, it works:
<code>with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    print(a)
</code>

