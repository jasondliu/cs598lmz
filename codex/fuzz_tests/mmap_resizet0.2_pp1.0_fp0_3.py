import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
I thought that the mmap object would be updated when the file is truncated.
Is there a way to make the mmap object aware of the truncation?


A:

The mmap object is not aware of the truncation because the file is not truncated.
The file is truncated when the file descriptor is closed.
So the following code works:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    f.close()
    a = m[:]
    print(a)
</code>

