import bz2
bz2.BZ2File("test.txt.bz2")
</code>
Here is the error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/home/kostas/PycharmProjects/ENV/local/lib/python2.7/site-packages/bz2.py", line 240, in __init__
    self._fp = open(filename, mode + "b")
IOError: [Errno 2] No such file or directory: 'test.txt.bz2'
</code>
I've tried the same in 2 different computers and the error remains. I don't think it is a problem with python-bz2 because I've tested the code in my laptop.
Any advice?


A:

<code>open</code> opens a file relative to <code>cwd</code>, so it should be:
<code>bz2.BZ2File("/home/kostas/PycharmProjects/ENV/test.
