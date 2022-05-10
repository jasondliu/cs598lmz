import types
types.ClassType
</code>
This is the error I'm getting:
<code>Traceback (most recent call last):
  File "&lt;pyshell#0&gt;", line 1, in &lt;module&gt;
    import types
  File "C:\Python26\lib\types.py", line 172, in &lt;module&gt;
    import functools
  File "C:\Python26\lib\functools.py", line 20, in &lt;module&gt;
    import copy
  File "C:\Python26\lib\copy.py", line 52, in &lt;module&gt;
    import weakref
  File "C:\Python26\lib\weakref.py", line 14, in &lt;module&gt;
    from _weakref import (
ImportError: cannot import name _remove_dead_weakref
</code>
How do I fix this?


A:

Looks like a bug in Python 2.6.6. Found a workaround from this thread.
<code>import site
site.addsitedir(r"
