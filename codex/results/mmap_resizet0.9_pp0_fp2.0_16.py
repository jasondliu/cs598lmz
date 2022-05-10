import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # Crash happens here.
</code>
I would expect <code>a</code> to either be empty or raise an exception. According to http://bugs.python.org/issue18014 this should already be fixed in Python 3.4.
What am I missing?


A:

I can't reproduce this. FWIW, this is my output (three times, same results):
<code>a = m[:]
Traceback (most recent call last):
  File "mmap2.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Edit: Never mind, I can reprocude it from a fresh startup of IDLE, but not from Python (Win 7, Python 3.4.1)
Edit: Changed code to use Python 3 specific syntax.

