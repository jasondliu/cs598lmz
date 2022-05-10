import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In the last line I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is wrong size
</code>
I've also created this test which shows the problem:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    print(m[:])
</code>
Here are the results of running this test with python 2 and python 3:
Python 2:
<code>$ python2 test.py

$
</code>
Python 3:
<code>$ python3 test.py

Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    print(m[:])
ValueError: mm
