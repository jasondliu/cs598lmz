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
Why does this happen?


A:

You are getting that error because the <code>mmap</code> object is no longer valid after you truncate the file.  You can see this in the documentation:
<blockquote>
<p>The file must exist. It is opened and closed by the constructor, and
  may be reopened and closed by the close() method. The file may not be
  resized while the mmap object exists. The file may be closed without
  closing the mmap object, but the inverse is not true. If the file is
  closed before mmap.close() is called, the mmap object raises an
  exception on any attempt to use it.</p>
</blockquote>

