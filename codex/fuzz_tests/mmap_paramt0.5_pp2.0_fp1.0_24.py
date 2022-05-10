import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'0'
    m.close()
</code>
The above code will raise an exception:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'0'
TypeError: 'mmap.mmap' object does not support item assignment
</code>
But if I change the first line of the code to
<code>with open('test', 'w+b') as f:
</code>
then it will work.
So why does <code>r+b</code> mode not work?


A:

From the docs:
<blockquote>
<p>If <code>&lt;code&gt;length&lt;/code&gt;</code> is 0, the maximum length of the map is the current size of the file when <code>&lt;code&gt;mmap&lt;/code&gt;</code> is called. <strong>If the file is extended while the memory map is alive, the extra memory is
