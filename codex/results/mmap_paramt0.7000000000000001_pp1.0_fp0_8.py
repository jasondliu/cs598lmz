import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
I'm getting the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    m[0] = bytes(2)
TypeError: mmap can't modify a readonly memory map
</code>
I'm not sure why this is the case, because I'm providing the <code>r+</code> flag to the <code>open</code> call.

