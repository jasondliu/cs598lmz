import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>

use <code>os</code> module:
<code>import os

with open('test', 'w') as f:
    f.write('a')

os.truncate('test', 0)

with open('test', 'r+') as f:
    f.read()
</code>



A:

Here's the solution that worked for me. I've adapted the second example you provided.
<code>os.truncate(file_path, 0)
with open(file_path, 'w') as file:
    file.write("")
</code>

