import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This gives me the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 6, in &lt;module&gt;
ValueError: cannot mmap an empty file
</code>
I know that I can't use <code>mmap.mmap()</code> with an empty file, but what I don't understand is why I can't read from it, even though I opened it with the <code>r+</code> mode.
If I create a new <code>mmap.mmap()</code> object after truncating the file, it works, but I don't want to do that.
I'm using Python 3.7.0 on Ubuntu 18.04.


A:

It's a bit of a hack, but you can use <code>mmap.ACCESS_READ</code> to read from an empty file.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
