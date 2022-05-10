import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(1)

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
</code>
This code gives the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m[0] = bytes(1)
TypeError: must be read-write buffer, not bytes
</code>
I also tried <code>m[0] = bytes(1)[0]</code> but that also doesn't work.


A:

You are trying to assign a byte to a slice of a bytes object.  That doesn't make sense.  You need to assign the bytes object to the slice.
<code>m[0:1] = bytes(1)
</code>

