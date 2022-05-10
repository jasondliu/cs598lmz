import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
However, when I try the same thing with a GDBM database, I get the following error:
<code>with shelve.open('test') as db:
    db['test'] = 1

with shelve.open('test', flag='r+') as db:
    m = mmap.mmap(db.dict.fno(), 0)
    m[0] = bytes(2)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 4, in &lt;module&gt;
  File "/usr/local/Cellar/python3/3.6.0_2/Frameworks/Python.framework/Versions/3.6/lib/python3.6/mmap.py", line 284, in __new__
    m = mmap_module.mmap(f.fileno(), map_size, access=access, offset=offset)
OverflowError: mmap length is greater than file size
</code>
I have no idea why the mmap length is greater than
