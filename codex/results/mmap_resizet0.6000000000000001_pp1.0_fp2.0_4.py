import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
When the program is run, it raises the following exception:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap closed or invalid
</code>
Is it possible to truncate the file without closing the mmap? If it is not possible, how can I truncate the file without leaking the mmap contents?
The reason I want to truncate the file is that I want to write the mmap contents to the file, but I want to write only the part that is actually used, which is much shorter than the whole mmap.


A:

The Python <code>mmap</code> module doesn't support truncating the underlying file while the map is still open.  The best you can do is unmap the file and then truncate it.
<code>m.close()
os.truncate(filename, length)
</code>
If you need to keep the map open, then you'll have to write to a temporary file and swap it in
