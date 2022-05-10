import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
However, if I change the first line to:
<code>with open('test', 'w+b') as f:
</code>
it will produce an <code>OSError: [Errno 15] Bad file descriptor</code>. This happens on both Python 2.7 and 3.6.
Why is this happening?


A:

The python documentation is a good start:
<blockquote>
<p>“b” appended to the mode opens the file in binary mode: now the data
  is read and written in the form of bytes objects. This mode should be
  used for all files that don’t contain text.</p>
<p>“r+” opens the file for both reading and writing.</p>
<p>“w+” opens the file for both writing and reading. Truncates the file to
  0 bytes.</p>
</blockquote>
The "w+" flag will result in opening a new, empty file, therefore the <code>mmap</code> cannot allocate a map on that file.
It will result in an <code>
