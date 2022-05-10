import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I would expect the <code>mmap</code> object to be updated when the file is truncated. Is this a bug or am I missing something?
I'm using Python 3.5.2 on Windows 10.


A:

The problem is that you are trying to use the <code>mmap</code> object after the file has been truncated.
The <code>mmap</code> object is a view of the file, and when the file is truncated, the view is no longer valid.
If you want to truncate the file and keep the <code>mmap</code> object, you have to do it in two steps:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0
