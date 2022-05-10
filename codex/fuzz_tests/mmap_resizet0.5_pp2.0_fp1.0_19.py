import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I'm using Python 3.4, but I think this makes no difference.
I get this error:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I'm not sure if this is a bug or if I'm doing something wrong.
If I don't truncate the file and just read the contents, it works fine.

