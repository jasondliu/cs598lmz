import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
However, the last line in the code above will throw <code>ValueError: memory mapping closed</code>. So I am wondering if there is any way I can avoid obtaining content of the file before calling truncate, and then after truncating, obtain the same content again.


A:

You can flush the changes made by your truncate:
<code>f.truncate()
m.flush()
</code>
This will also ensure that the file is closed as soon as possible (it'll <code>close</code> once the next read operation is done). If you don't call close explicitly, you may wait until the next garbage collection cycle before new files can be created and you'll end up with the maximum number of open files under your process (e.g. 256), even if it's far, far more.

