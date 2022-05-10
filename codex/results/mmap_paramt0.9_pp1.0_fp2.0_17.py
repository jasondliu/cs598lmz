import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.move(0, 1, 4)
    m[0] = 5
    m.close()
</code>
Fails with:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    m[0] = 5
ValueError: mmap slice assignment is wrong size
</code>
What is correct way to achieve something like this?

