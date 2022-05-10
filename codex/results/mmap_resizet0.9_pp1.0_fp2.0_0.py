import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code ends not with a <code>ValueError</code> in a <code>WindowsError</code> and the traceback looks like this:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    a = m[:]
WindowsError: [Error 87] The parameter is incorrect
</code>
So what I'm asking is - is there any way I could catch Windows errors in Python, or is there any way I could track the state of the <code>m</code> object, to see if it's still valid?


A:

I don't think you can catch the exception, but you can try to avoid getting it. In the Python version I'm using (2.7.2, Windows 7), the mapping appears to be unaffected by the <code>truncate</code> call (i.e., you can still access that byte even after the underlying file has shrunk to zero bytes).
So it seems that the problem is not the truncation itself, but the fact that you're going to access the entire memory-mapped region. If you
