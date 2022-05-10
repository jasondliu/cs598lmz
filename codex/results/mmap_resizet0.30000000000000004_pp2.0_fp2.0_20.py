import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I am getting the following error:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I am trying to use the mmap module to create a memory mapped file in order to read and write to it. I am trying to create a memory mapped file that is 1 byte long, and then truncate it to 0 bytes. I am then trying to read the contents of the memory mapped file. However, the read operation is failing with the error above.
I am using Python 3.6.5 on Windows 10.


A:

The <code>mmap</code> object is a view into the file, so when you truncate the file, the view is no longer valid.
You can use <code>mmap.resize</code> to resize the file and the view, but you can't make the file smaller than the view.

