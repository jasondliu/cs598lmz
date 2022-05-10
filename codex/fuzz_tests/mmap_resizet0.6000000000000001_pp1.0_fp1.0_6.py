import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get this error:
<blockquote>
<p>ValueError: mmap can't resize a file which is using mmap.</p>
</blockquote>
I've looked at the mmap documentation and can't find anything related to what I want to do.  Is there a way to close the mmap without closing the file?  Or is there a better way to truncate the file without affecting the mmap?
(I know that the mmap is not needed in this example, but in my real code I don't know if the mmap is needed or not until after I've done a bunch of work with the file).


A:

You can't, but you can just map the whole file again after truncating it.

