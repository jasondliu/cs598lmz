import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
The above code will run fine, but it will not update the file size.
What I found to work is using a temporary file, and then rename it:
<code>import os
import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
    f.flush()

os.rename('test', 'test2')
os.rename('test2', 'test')
</code>
But this is ugly, and has race conditions. Is there a better way?
Note that the file is written to on a separate process, and then read by the current process with a <code>mmap</code> call.


A:

What about using <code>truncate</code>?
<code>import os
import mmap
