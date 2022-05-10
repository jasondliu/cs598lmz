import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 2
</code>
However, I would like to be able to only read the file, without the need to open it in "write"-mode. Python's documentation states that:
<blockquote>
<p>If length is 0, the maximum length of the map will be the current size of the file when mmap is called.</p>
</blockquote>
So I changed the last line to:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
</code>
But this throws the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
ValueError: mmap length is zero
</code>
Why is there a length restriction on the read-only mode? Is there any way to go around this?
Note: I'm using Python 3.4.


A:

Zero is a valid length argument
