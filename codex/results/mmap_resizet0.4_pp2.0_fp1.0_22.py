import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This gives me an error:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: readonly buffer
</code>
How can I get the data from the file?


A:

<code>mmap</code> objects are read-only by default. You can create a read-write <code>mmap</code> object by passing <code>mmap.ACCESS_WRITE</code> as the access parameter:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
</code>

