import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
I got the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I think I have the same problem as in this question: mmap.mmap() error: ValueError: mmap length is zero
But I don't know how to fix it. I tried to use <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code> but it didn't work.
What do I do wrong?

