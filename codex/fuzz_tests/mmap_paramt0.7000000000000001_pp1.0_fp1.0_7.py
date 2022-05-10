import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(20)
    m.close()
</code>
In Python 3.3.0, this code works fine.  In Python 2.7.3, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m.resize(20)
ValueError: new size must be a multiple of the mmap granularity
</code>
What is the mmap granularity, and why does this code work in 3.3.0 but not 2.7.3?


A:

As far as I can tell, the problem is that mmap.mmap() always assumes that the file is opened with a granularity of mmap.ALLOCATIONGRANULARITY, which is always 4096 on my system.  It doesn't matter how the file was actually opened.  I found the source code here:
http://hg.python.org/cpython/file/3.3/Modules/mmapmodule.c

