import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
raises
<code>Traceback (most recent call last):
  File "main.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
This is somewhat counter-intuitive, I would expect either to work just fine, or to get something like <code>file is already mapped</code> or <code>file is already truncated</code> or something.
Is there a good way to avoid this, short of unmapping the file first?


A:

This is a bug, or at least a pretty significant limitation of the current mmap module. It is not possible to re-use a mmap object if the underlying file is closed, so it isn't as simple as just unmapping the file first. The only workarounds that I'm aware of are to either open a new file (if truncating is optional), or to just leave the file open after truncating.
The feature request for this is here:
http://bugs.python.org/issue23807

