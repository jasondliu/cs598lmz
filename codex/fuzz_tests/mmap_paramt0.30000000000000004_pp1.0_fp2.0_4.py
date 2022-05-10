import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = b'\x00'
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'\x00'
TypeError: 'mmap.mmap' object does not support item assignment
</code>
I am using Python 3.6.5.
What am I doing wrong?


A:

You need to use the <code>access</code> parameter to <code>mmap.mmap</code> to specify that you want to be able to write to the memory map.
<code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
</code>

