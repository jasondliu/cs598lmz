import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I'm getting:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
TypeError: mmap slice indices must be integers or None or have an __index__ method
</code>
What is the proper way of doing this?


A:

It was a bug in python, fixed in python 3.5.1

