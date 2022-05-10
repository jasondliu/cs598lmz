import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
And here's the traceback:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
What I'm trying to accomplish is to have a process write to a file, and another process read from it. The file must be read from the beginning every time, and I'd really rather avoid using named pipes.
I've also tried using the <code>f.fileno</code> that is passed to <code>mmap</code> instead of the original file, but it does the same thing.


A:

You can't use a file-based mmap after truncating the file. The problem is that when the mmap is created the file size is recorded, and if the size changes the mmap is no longer valid.
To do what you want, you need to create the mmap with a length of 0 and use <code>f.truncate(0)</code> to truncate the file. This will leave the mmap intact, but you'll
