import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

with open('test', 'rb') as f:
    b = f.read()

a == b
</code>
I am getting:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    a == b
ValueError: mmap can't resize memory maps backed by files
</code>
Is there a way to avoid the error?


A:

This is not quite what you asked for, but you can avoid the error by not reading from the map after truncation (but before closing it).
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    # a = m[:]
    m.close()
    # uncommenting these two ensures that the error is raised
    # a = m[:]
    # m.close()

with open('test', 'rb') as f:
    b = f.read()

assert b == b''

