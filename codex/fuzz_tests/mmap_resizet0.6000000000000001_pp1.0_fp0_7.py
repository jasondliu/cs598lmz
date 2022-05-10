import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
Result:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot read from closed file
</code>
What's the reason for this, and is there a way to read from a closed mmap object?


A:

The reason is that mmap objects are not file objects. They are a view into a file, and when you close the file, the view is invalidated.
To answer the question in the title, you can't read from a closed mmap object, because it isn't closed. It's just invalidated.

