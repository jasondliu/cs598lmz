import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('x')
    m.close()

with open('test', 'r') as f:
    print(f.read())
</code>
I get the error:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 5, in &lt;module&gt;
    m[0] = ord('x')
ValueError: must have exactly one item to unpack
</code>
I've tried many different variations of the script, but I can't get it to work.
I'm running python 3.5.2 on Linux Mint 18.2.


A:

This is because you're trying to assign to a byte in a <code>bytes</code> object.
<code>&gt;&gt;&gt; m = bytes(1)
&gt;&gt;&gt; m[0] = ord('x')
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'bytes'
