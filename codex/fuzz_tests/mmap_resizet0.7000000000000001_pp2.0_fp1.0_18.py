import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    del m
    print(a)
</code>
Running this code prints <code>b'\x00'</code>. I would expect an <code>IndexError</code> instead.
How is <code>del m</code> not causing the <code>IndexError</code>?


A:

I found out that if I use the <code>access</code> parameter of <code>mmap.mmap</code> to make the memory map read-only, then I get the desired exception.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    f.truncate()
    a = m[:]
    del m
    print(a)
</code>
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m
