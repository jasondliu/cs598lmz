import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
    m.resize(4)
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(len(m))  # prints `4`
</code>
However, if the resize happens to result in a smaller size, and the data is late-written to the new file, none of the data gets written:
<code>from __future__ import print_function
import mmap

with open('test', 'wb') as f:
    f.write(bytes(100))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 100, access=mmap.ACCESS_WRITE)
    m.resize(4)
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(len(m))  # prints `4`
   
