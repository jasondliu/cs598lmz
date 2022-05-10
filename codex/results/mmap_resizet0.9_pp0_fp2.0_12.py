import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # &lt;- this raises an exception, of course
</code>
I want the truncate to fail if the memory mapped segment is not empty after the write.
I consider changing the callback to <code>munmap()</code> on every write attempt.


A:

<code>mmap</code> allows you to specify a length at construction time (the size of the file, by default).  This length is the maximum addressable memory area for the object.  Attempts to access memory beyond this past memory limit will raise the exception you observe.  See the <code>mmap</code> documentation for more information.
What you've done here is suggest that you want to insert a single character into the file, but leave enough room for a lot more data.  This means that <code>m[1:]</code>, the remainder of the memory area you allocated, is still assigned to the file, but you've truncated away from the file anything beyond the single-character insertion.  Attempts to access that memory area will raise an exception because it's now invalid.
Instead, you should use <code>m[0]</code> or <code>m[:
