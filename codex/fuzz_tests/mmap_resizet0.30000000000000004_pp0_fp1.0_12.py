import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>.
I expected the output to be <code>b'\x01'</code>.
Why is the output <code>b'\x00'</code>?


A:

The <code>mmap</code> object is a view into the file.  When you truncate the file, the view is no longer valid.  You can see this by trying to access the <code>mmap</code> object after truncating the file:
<code>&gt;&gt;&gt; m[:]
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
ValueError: mmap slice assignment is wrong size
</code>

