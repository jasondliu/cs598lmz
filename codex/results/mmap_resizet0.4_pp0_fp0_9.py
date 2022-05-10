import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
Why is this? What is the proper way to truncate a file and have the mmap still be valid?


A:

You need to call <code>m.resize</code> after truncating the file.
<code>m.resize(0)
</code>

