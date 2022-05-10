import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)

with open('test', 'rb') as f:
    print(f.read())
</code>
This works fine on Linux and Windows, but on macOS, the file is not updated.
I also tried adding <code>m.flush()</code> after the assignment, but it doesn't change anything.
What am I doing wrong?


A:

I found the solution here:
https://docs.python.org/3/library/mmap.html#mmap.mmap
<blockquote>
<p>The file cannot be larger than the addressable space of the process.
  On some systems, you may need to specify the length when you create
  the mmap object, in order to map the whole file.</p>
</blockquote>
So, I had to specify the size when creating the mmap object:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap
