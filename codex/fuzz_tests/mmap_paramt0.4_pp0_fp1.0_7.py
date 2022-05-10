import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x02'
    m.close()
</code>
This works fine on Windows and Linux, but on Mac OS X I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'\x02'
TypeError: mmap slice assignment is restricted to byte stores
</code>
Is there a way to do this on Mac OS X?


A:

You can't assign a <code>bytes</code> object to a <code>mmap</code> slice, but you can assign a single byte:
<code>m[0] = b'\x02'[0]
</code>

