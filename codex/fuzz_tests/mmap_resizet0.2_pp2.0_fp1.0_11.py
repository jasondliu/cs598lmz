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
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I would expect the <code>mmap</code> to be updated with the truncated file.
I am using Python 3.6.5 on Ubuntu 18.04.


A:

You can't use <code>mmap</code> on a file that has been truncated.
<blockquote>
<p>If the file is resized, the mmap cannot be used.</p>
</blockquote>
https://docs.python.org/3/library/mmap.html

