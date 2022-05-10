import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
But it fails with:
<code>Traceback (most recent call last):
  File "test.py", line 7, in &lt;module&gt;
    a = m[:]
ValueError: cannot resize memory map
</code>
Is there any way to extend the mmap?
I know I can just create a new one, but that's not what I'm asking for.
I'm asking for extending the existing mmap, not creating a new one.

