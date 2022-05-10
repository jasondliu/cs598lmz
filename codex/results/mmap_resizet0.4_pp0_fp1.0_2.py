import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I am getting an error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
The code works fine if I use <code>with open('test', 'r+b') as f:</code> instead of <code>with open('test', 'wb') as f:</code>.
How can I truncate the file and read from the mmap?


A:

You can't.  The mmap is attached to a file descriptor, and the file descriptor is attached to a file.  If you truncate the file, the mmap is no longer valid.

