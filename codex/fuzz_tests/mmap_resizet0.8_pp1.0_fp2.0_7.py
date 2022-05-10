import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
Where <code>test</code> is a file with size 1 byte.
This produces the following error:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: mmap length is zero
</code>
I understand that the file being mapped is empty, but I would like to map it as is (empty).
Is there a way to do this in python?
Thanks!


A:

Try this instead:
<code>with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    a = m[:]
    m.close()
</code>
Remember that the <code>size</code> argument to the <code>mmap()</code> function is advisory. It only tells the kernel what kind of map you want to create. If you want
