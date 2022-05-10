import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>
However, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'\x00'
ValueError: readonly buffer
</code>
I have tried all the different flags for <code>mmap</code> (e.g. <code>mmap.MAP_PRIVATE</code>), but none of them seem to work. I have also tried using <code>mmap.ACCESS_WRITE</code> and <code>mmap.ACCESS_COPY</code> as the second argument to <code>mmap</code>, but that did not work either.
How can I get this to work?


A:

You need to use <code>mmap.ACCESS_WRITE</code> as the second argument to <code>mmap</code>.
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS
