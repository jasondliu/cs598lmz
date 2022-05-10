import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = bytes(2)
</code>
Error:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 8, in &lt;module&gt;
    m[0:1] = bytes(2)
ValueError: mmap assignment is wrong size
</code>
What I want to do is to write number 2 to the file. I tried <code>bytes(2)</code> and <code>bytearray([2])</code> without luck. What is the proper way to do it?


A:

The error message is pretty clear: "mmap assignment is wrong size".
You need to assign a <code>bytes</code> object of length 1:
<code>m[0:1] = bytes([2])
</code>

