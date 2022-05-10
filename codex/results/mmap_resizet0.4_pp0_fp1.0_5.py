import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises an exception:
<code>Traceback (most recent call last):
  File "C:/Users/User/PycharmProjects/test/test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I understand that the file is truncated and the mmap object is not updated, but I don't know how to update it.
So, how can I update the mmap object after truncating the file?


A:

You have to call <code>m.resize(new_size)</code> to resize the mmap object.

