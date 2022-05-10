import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I'm using Python 3.5.2.
Is there a way to avoid this exception?


A:

The problem is that you're trying to read from the <code>mmap</code> object after you've truncated the file.
The <code>mmap</code> object is still pointing to the old file size, and so it's trying to read from the old file size.
If you want to read from the new file size, you need to create a new <code>mmap</code> object.

