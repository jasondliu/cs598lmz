import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    print(m[:])
</code>
this will report:
<code>[1]    1837 segmentation fault  python test.py
</code>
However, if I use a larger buffer, such as:
<code>m = mmap.mmap(f.fileno(), 20)
</code>
then the code works fine:
<code>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
</code>
It looks like <code>mmap</code> can't handle buffering for a large file, but this is a very tiny file.
How can I use <code>mmap</code> with a small file?


A:

Use the <code>length</code> parameter to <code>mmap</code> instead of <code>1</code>.

