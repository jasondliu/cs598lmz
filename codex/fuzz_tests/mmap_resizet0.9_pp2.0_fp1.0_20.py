import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
And here is the error that I get:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot read from mmap - mprotect failed
</code>
Searching for this error, I found this answer and this other one, but I couldn't get a solution that would work.
I'm using Android 9.0, Python 3.7.1, and Cython==0.29.9. I'm definitely willing to try a different version of those if necessary.
This issue started when I got a new phone. The error did not occur on the previous phone, which used Android 8.0 and Python 3.7.1, but I didn't try Cython at the time.


A:

The solution is to list the files to import explicitly in the <code>sources</code> part of the <code>setup.py</code>, like so:
<code>include_packages=['*']
sources=['file1.pyx', 'file2.pyx', 'file3
