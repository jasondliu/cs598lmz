import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>
This code works fine on my machine, but on a server I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'\x00'
ValueError: mmap assignment is read-only
</code>
I have tried to run the code with <code>sudo</code>, but it doesn't help. I have also tried to use <code>mmap.ACCESS_WRITE</code> instead of <code>0</code>, but it doesn't help either.
What can be the reason of this error?


A:

I've found the reason. The file was opened by another process.

