import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
As expected, I get the error (which is not surprising):
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
However, the following code:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.seek(2)
    f.truncate()
    a = m[:]
</code>
works just fine!
So, is this a bug in python or is this the expected behavior?
I tried it on python 2.7.13 and 3.6.2 and it seems to be the same.

