import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(3))
    m.close()
</code>
I get:
<code>Traceback (most recent call last):
  File "C:\Users\User\Desktop\test.py", line 8, in &lt;module&gt;
    m.write(bytes(3))
ValueError: cannot resize a wrapped mmap object
</code>
Why?

