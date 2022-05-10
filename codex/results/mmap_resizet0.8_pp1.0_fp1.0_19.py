import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>


A:

This is true for Python 3.3
<code>Traceback (most recent call last):
  File "&lt;pyshell#5&gt;", line 1, in &lt;module&gt;
    m[:]
ValueError: cannot resize a readonly memory mapping
</code>
This is true for Python 3.4
<code>Traceback (most recent call last):
  File "&lt;pyshell#7&gt;", line 1, in &lt;module&gt;
    m[:]
ValueError: cannot resize a readonly or copy-on-write memory mapping
</code>
The error message has been improved in Python 3.4.

