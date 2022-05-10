import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # This will give an error, as expected
</code>
The error I get:
<code>Traceback (most recent call last):
  File "mmaptest.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
As the traceback shows, the error occurs when I try to copy the mmap to a string to print. However, if I change the file size of the open file in the traceback, the error does not occur. What I don't understand, is how it is possible to have this code execute without a <code>ValueError</code> when it seems I'm accessing a mmap after it's file has been truncated. Is it POSSIBLE that when I call <code>m=mmap.mmap(f.fileno(), 0)</code>, it doesn't actually create an instance of a mmap until I use the map? That seems to be the only logical explanation, but the mmap docs make no mention that this is the case. Furthermore, the error occurs on my specific machine but not a friend's. So is there some other
