import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
And I get the following error
<code>Traceback (most recent call last):
  File "test_mmap.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot read memory at address 0x0
</code>
But when I manually close the memory map before truncating, it works:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()
    f.truncate()
    a = m[:]
</code>
This is just a simple example, but in my real code, I have a file object that I've opened with <code>mmap.mmap</code> and I want to continue using it (just read-only) after I resize the file. I'm not sure I am correctly closing memory maps, and I don't know if maybe this is a bug, so I am asking here.


A:


