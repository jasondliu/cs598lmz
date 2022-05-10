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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I am using Python 3.4.3 on Windows 7.
I have also tried using <code>m.seek(0)</code> before reading from the mmap, but that didn't help.


A:

You can't truncate a file that is mmap'd.
From the docs:
<blockquote>
<p>The file must not be larger than can be represented by an off_t (an
  OS-dependent quantity, but usually a 32-bit signed integer). If the
  file is truncated, the contents of the mmap between the old and new
  end of the file are lost.</p>
</blockquote>

