import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I expect <code>a</code> to contain <code>bytes(1)</code> or <code>b'\x00'</code>.
What is going wrong?


A:

The problem is that you first create a memory map for the whole file, and then truncate the file. As you truncate the file, it is no longer a valid memory map.
The solution is to truncate the file before creating the memory map.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    print(a)
</code>

