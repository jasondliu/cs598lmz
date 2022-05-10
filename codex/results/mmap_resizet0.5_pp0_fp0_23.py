import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This causes a <code>ValueError</code> on the last line, because <code>m</code> is still a reference to the old memory.
I would like to be able to truncate the file, and then have the <code>mmap</code> object automatically resize itself to match.  Is there a way to do this?  I've looked through the <code>mmap</code> docs, but I can't find anything.


A:

I don't think there's a way to do this with the built-in <code>mmap</code> module.
However, there is a third-party module, <code>mmapfile</code>, that does what you want.
<code>&gt;&gt;&gt; import mmapfile
&gt;&gt;&gt; with open('test', 'wb') as f:
...     f.write(bytes(1))
... 
&gt;&gt;&gt; with mmapfile.mmapfile('test', 'r+') as m:
...     m.truncate()
...     a = m[
