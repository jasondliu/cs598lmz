import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
</code>
I get the error:
<code>Traceback (most recent call last):
  File "C:/Users/mike/Desktop/test.py", line 6, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: mmap length is zero
</code>
I was expecting it to work, but it doesn't. Any ideas?


A:

You should use <code>mmap.mmap(f.fileno(), 1)</code> instead.
<code>mmap.mmap(f.fileno(), 0)</code> means that you want to map the whole file, but you are trying to map a file with a length of 1, so you should use <code>mmap.mmap(f.fileno(), 1)</code> instead.

