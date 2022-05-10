import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises an <code>OSError</code> with the message <code>mmap: can't extend file</code>.
This is explained in the documentation:
<blockquote>
<p>All modifications to the data are written directly to the mmap’ed file. If you mmap a file that does not exist, the file will be created and the size you specify in the length argument will be the size of the mmap’ed file. If you mmap a file that does exist, the file cannot be resized.</p>
</blockquote>
So the <code>truncate()</code> call is causing the file to be resized, which is not allowed.
The workaround is to use <code>ftruncate()</code> instead:
<code>import os
import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    os.ftruncate(f.fileno(), 0)
