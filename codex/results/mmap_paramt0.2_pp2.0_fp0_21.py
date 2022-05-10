import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())
</code>
This works fine on Linux, but on Windows I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: cannot mmap an empty file
</code>
I'm using Python 3.6.1 on Windows 10.
What am I doing wrong?


A:

The problem is that you are opening the file with <code>wb</code> mode, which truncates the file.
From the docs:
<blockquote>
<p>'w' for only writing (an existing file with the same name will be erased),</p>
</blockquote>
You should open the file with <code>r+b</code> mode, which allows both reading and writing, and doesn't truncate the file.

