import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last <code>m[:]</code> call causes:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    a = m[:]
ValueError: cannot read memory at address 0x7fffa0c00050
</code>
So, is there a way to re-map the file to the original address, like this?
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.remap(f.fileno(), 0)
    a = m[:]
    m.close()
</code>


A:

No; the mmap object maintains a reference to the file descriptor so that it can check the length of the file on each access. The effect of truncating the file is that the file is no longer accessible. 

