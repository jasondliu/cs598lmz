import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print('mmap before:', m[:1])
    m[:1] = b'\00'
    m.flush()
    m.close()

with open('test', 'rb') as f:
    print('read before:', f.read(1))

import os
os.system('echo "read after: $(cat test)"')
</code>
The result of running the above code is:
<code>mmap before: b'\x01'
read before: b'\x00'
read after: 
</code>


A:

From the documentation: 
<blockquote>
<p>The mmap() function can be used to map device special files like /dev/mem or /dev/kmem, or regular files that have been opened with the O_DIRECT flag (since Linux 2.4.10 and 2.5.47). </p>
</blockquote>
You can thus expect correct behaviour only on <code>/dev</code> files.
Moreover, flushing the memory map does not flush the file. You have to do it manually.
