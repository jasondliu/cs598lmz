import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I got
<code>Traceback (most recent call last):
  File "mmap_truncate.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot resize memory map
</code>
So it is not possible.
But is there a way to make it possible? I mean, is it possible to make it without writing/reading/mmap'ing the whole file?
I have huge binary files and I need to cut some part of it.

