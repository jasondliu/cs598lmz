import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This gives me the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
What is the correct way to do this?


A:

The problem is that you're truncating the file after you've opened the <code>mmap</code> object.  The <code>mmap</code> object is still trying to access the file at the original size.  If you move the <code>truncate()</code> call before the <code>mmap</code> call, it will work.

