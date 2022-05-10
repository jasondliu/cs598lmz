import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap closed or invalid
</code>
Is there a way to have a file object and a mmap object both open at the same time?


A:

No, you can't.
The mmap object is a wrapper around the file descriptor, and you're closing the file descriptor.
You can use the <code>mmap.mmap()</code> function to create a memory-mapped file object, but you have to pass it a valid file descriptor.

