import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It works on Linux, but on Windows it raises an exception:
<code>Traceback (most recent call last):
  File "C:\Python34\Lib\site-packages\mmap.py", line 757, in __getitem__
    res = self.read(length)
ValueError: can't read from closed file

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
  File "C:\Python34\Lib\site-packages\mmap.py", line 759, in __getitem__
    raise ValueError('mmap closed or invalid')
ValueError: mmap closed or invalid
</code>
The same code works with python 3.3.
Is this a bug or a feature?
Is there a way to make it work?
Note that it is important that the <code>truncate</code> call is directly before the <code>mmap[:]</code> call.


A:

I suspect
