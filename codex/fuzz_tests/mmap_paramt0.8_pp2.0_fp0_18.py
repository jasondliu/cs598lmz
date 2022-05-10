import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(1)
</code>
I got this error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 5, in &lt;module&gt;
ValueError: memoryview: slicing is disallowed
</code>
I tried to use <code>m.move()</code> instead of the <code>[:]</code> assignment, but then I got the error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 4, in &lt;module&gt;
ValueError: memoryview: underlying buffer is read-only
</code>
I also tried <code>m.write()</code>. I got this same error.
How do I write to the entire file, without having to use a file object and having to read the entire file, then use the object to write, then read the entire file again, just to write to 1 byte in the entire file? I don't want to have to call <code>f.seek()</code> and <code>f.
