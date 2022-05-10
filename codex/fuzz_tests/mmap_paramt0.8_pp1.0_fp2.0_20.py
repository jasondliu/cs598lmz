import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
    m.close()
</code>
Which throws 
<code>Traceback (most recent call last):
  File "C:\Users\sidharth.m\Desktop\mmap\test.py", line 10, in &lt;module&gt;
    m[0] = b'2'
TypeError: 'mmap.mmap' object does not support item assignment
</code>
I know that mmap creates a read-only copy of the file in memory, but I want to update the bytes. How should I do it?


A:

MMap objects are read-only.  You open the file for writing.  You just need to open the file for read and write.
<code>f = open('test', 'wb')
f.write(bytes(1))
f.close()

f = open('test', 'r+b')
m = mmap.mmap(f.fileno(), 0)
m[0] = b'2'
m.close()
print(open('test').read())
</code
