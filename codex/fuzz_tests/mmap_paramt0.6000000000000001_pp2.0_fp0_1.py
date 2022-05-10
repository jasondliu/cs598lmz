import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m.close()
</code>
I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m.resize(2)
OSError: [Errno 22] Invalid argument
</code>
Why does this not work? Is there a way to make this work?


A:

You need to specify a length when opening the mmap:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m.resize(2)
    m.close()
</code>

