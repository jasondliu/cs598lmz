import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code does not raise an exception, but the value of <code>a</code> is unchanged.
Is there a way to get the updated value of <code>m</code> after <code>f.truncate()</code>?


A:

I don't think you can do what you want to do.
The <code>mmap</code> object only exists as a view into the file, and it is only valid so long as the file can be opened.  When you truncate the file, it means that the file no longer has the contents that are reflected in the <code>mmap</code> object.  In fact, trying to truncate the file at all is invalid behavior.  The documentation says:
<blockquote>
<p>The file attribute of an mmap object is not usable after the object has been closed.</p>
</blockquote>
It is not clear from your example why you are trying to truncate the file.  Perhaps if you explain what you are trying to accomplish, someone can offer an alternative approach.

