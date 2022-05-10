import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.seek(0)
    print(m.read(1))
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 5, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
TypeError: mmap length is positive
</code>
I'm using Python 3.6.5.


A:

You need to specify the length of the file as the second argument to <code>mmap.mmap</code>.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m.write(bytes(1))
    m.seek(0)
    print(m.read(1))
</code>

