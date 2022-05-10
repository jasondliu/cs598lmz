import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code gives the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I was expecting the <code>mmap</code> object to be updated when the file was truncated, but it seems that it is not the case.
Is there a way to make it work?


A:

You need to resize the mmap object after truncating the file:
<code>m.resize(0)
</code>

