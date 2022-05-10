import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.flush() # flush out before mmap object is closed

print(a)
</code>
this works all the time. On the other hand, if you remove <code>f.truncate()</code>, something like this can happen:
<code>Traceback (most recent call last):
  File "C:/Users/Andrew/Desktop/test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: memory mapping cannot be larger than file
</code>
However, it's still not guaranteed and it seems unreliable.

