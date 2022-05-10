import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('2')
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    m[0] = ord('2')
TypeError: 'mmap.mmap' object does not support item assignment
</code>
I'm running Python 3.5.1 on Windows 10.


A:

The <code>mmap</code> object is read-only by default. You need to pass <code>access=mmap.ACCESS_WRITE</code> to the <code>mmap</code> constructor to be able to write to it.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = ord('2')
    m.close()
</code>
