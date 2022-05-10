import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
Print if <code>test</code> is <code>0x01</code>:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
Print if <code>test</code> is not <code>0x01</code>:
<code>b''
</code>
I.e. access to the file after <code>truncate</code> with <code>mmap</code> should never work.


A:

Passing a filename of an empty file to <code>mmap</code> is a good way to make a <code>ValueError: must have exactly one argument</code>.
Since <code>mmap</code> is close tot he base layer, it has no file data, only labels used by the operating system to find the data on a disk. 
To create an actual map, it needs that file id and a length. Since the length is zero, the <code>mm
