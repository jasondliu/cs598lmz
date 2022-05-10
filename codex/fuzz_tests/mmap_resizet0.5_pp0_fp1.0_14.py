import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # &lt;- this is the line that fails
</code>
The last line fails with the following exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is bigger than mmap size
</code>
I understand that the size of the memory map is no longer correct, but I'm not sure how to fix this. I can't just close the memory map and reopen it, because the file is already truncated.
What is the correct way to handle this situation?


A:

I think the problem is that you're not specifying the length of the memory map when you create it.  You should use something like this:
<code>with open('test', 'r+b') as f:
    length = os.stat(f.fileno()).st_size
    m = mmap.mmap(f.fileno(), length)
    f.truncate()
    a = m[:] # &lt;- this is the line that fails
</code>

