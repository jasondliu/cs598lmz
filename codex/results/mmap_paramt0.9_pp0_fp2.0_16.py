import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

m.seek(0)
</code>
I get the following error on the last line, as expected:
<code>Traceback (most recent call last):
  File "testfile.py", line 10, in &lt;module&gt;
    m.seek(0)
TypeError: seek() takes exactly 2 arguments (1 given)
</code>
But since I'm using Python 2, shouldn't I be using the old <code>seek()</code> interface which just takes the offset?


A:

You should use <code>mmap.mmap(f.fileno(), f.tell())</code> instead of <code>mmap.mmap(f.fileno(), 0)</code>.
Then you can change that line to <code>add_num = m.read_byte()</code> to read the value as an <code>int</code>.

