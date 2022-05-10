import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
Which gives the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
The file is empty, so I'm not sure why the length is zero.


A:

You're truncating the file after you create the mmap.  The mmap is tied to the file, so when you truncate the file, the mmap is also truncated.  If you move the <code>f.truncate()</code> call to before you create the mmap, it works as expected.

