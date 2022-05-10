import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine on Windows, but on Linux I get an <code>OSError: [Errno 22] Invalid argument</code> on the <code>m[:]</code> line.
I've tried using <code>mmap.ACCESS_READ</code> instead of <code>mmap.ACCESS_COPY</code>, but that doesn't seem to make a difference.
Is there a way to make this work on Linux?


A:

You can't use <code>mmap</code> on a file that has been truncated.
<blockquote>
<p>If the file is resized, the contents of the additional area are
  undefined. The file may not actually grow until the data is written
  to the file.</p>
</blockquote>

