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
It works fine on my machine, but on the other one I get:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
TypeError: '_mmap.mmap' object is not subscriptable
</code>
I've tried to google it, but I didn't find anything.
What can be the reason of this problem?

