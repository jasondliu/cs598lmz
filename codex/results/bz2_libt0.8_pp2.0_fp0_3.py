import bz2
bz2.BZ2File("/home/test/test/test.txt")

...

File "/usr/lib/python2.6/bz2.py", line 192, in __init__
if not isinstance(filename, basestring):
NameError: name 'basestring' is not defined
</code>
Python 2.6 is installed by building from source and I don't think 'basestring' is a global variable of 2.6 so how to fix it?


A:

<code>basestring</code> is only available in Python 2.x, not in Python 3.x:
<code>&gt;&gt;&gt; import sys
&gt;&gt;&gt; sys.version_info
sys.version_info(major=2, minor=6, micro=1, releaselevel='final', serial=1)
&gt;&gt;&gt; basestring
&lt;type 'basestring'&gt;
&gt;&gt;&gt; sys.version_info
sys.version_info(major=3, minor=2,
