import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'c'
    m.close()

with open('test', 'r') as f:
    print(f.read())
</code>
As you can see I'm writing a byte, and then I want to replace it with another byte. But this doesn't work. I'm getting the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    m[0] = b'c'
TypeError: 'mmap.mmap' object does not support item assignment
</code>
Why is this happening? I'm using python 3.3.3.


A:

The problem is that you are using <code>mmap</code> in read-only mode.  If you want to be able to write to the file, you need to use the <code>access=mmap.ACCESS_WRITE</code> parameter.  Note that you also need to open the file in write mode, <code>'r+b'</code>, rather than just read-only, <code
