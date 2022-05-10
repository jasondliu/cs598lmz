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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I'm not sure how to fix this.


A:

The <code>mmap.mmap</code> function takes a file descriptor, not a file object. It's best to avoid using the file object entirely.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    fd = f.fileno()
    m = mmap.mmap(fd, 0)
    f.truncate()
    a = m[:]
    print(a)
</code>

