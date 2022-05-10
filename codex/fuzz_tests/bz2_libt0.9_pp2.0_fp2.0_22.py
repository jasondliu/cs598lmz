import bz2
bz2.BZ2File(filename)
</code>
But getting error: 
<code>bz2.BZ2File(filename)
Traceback (most recent call last):
File "&lt;stdin&gt;", line 1, in &lt;module&gt;
File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/bz2.py", line 81, in __init__
    self.compress = compress
TypeError: a bytes-like object is required, not 'str'
</code>
I don't understand why is it. Any help?


A:

The error message is stating that they expect a bytes object, not a string. So you could do:
<code>with open(filename) as fh:
    data = fh.read().encode('utf-8')
    bz2.BZ2File(data)
</code>
note that you can't <code>open</code> something that was compressed as is, as <code>open</code> is for plain text/binary files. But
