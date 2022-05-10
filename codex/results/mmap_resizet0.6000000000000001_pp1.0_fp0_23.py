import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "C:\Users\Eugene\Desktop\py\mmap\test.py", line 12, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm confused because I thought that the offset is 0 by default. Also, I tried to use the <code>os.path.getsize</code> instead of <code>os.stat</code> but it didn't help.


A:

<code>mmap</code> has its own size information, which is independent of the actual file size. This is used to determine the length of the array.
The size of the <code>mmap</code> object is not updated when you truncate the file. This means that when you slice <code>m</code>, you are slicing into the middle of the file, where there is nothing.
If you want to get the contents of the file, you'll have to slice the <code>mmap</code>
