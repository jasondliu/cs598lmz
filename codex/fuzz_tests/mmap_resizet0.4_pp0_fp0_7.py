import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
I have a file with one byte. I open it with mmap, then truncate it and try to read the mmap. I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
I understand that the file is empty and I can't mmap it. But why does it work if I don't truncate it? I open the file with mmap, then I truncate it, then I try to read the mmap. I don't understand why it works if I don't truncate it.
I'm on Linux.


A:

You are using <code>mmap.mmap</code> which is different from <code>mmap.MAP_SHARED</code> and <code>mmap.MAP_PRIVATE</code>.
<blockquote>
<p>If fileno is not -1, the mmap() function maps the file specified by

