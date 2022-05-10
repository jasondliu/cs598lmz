import ctypes
ctypes.util.find_library('c')
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python2.6/ctypes/util.py", line 36, in find_library
    return _get_sonames(_findLib_gcc(name))
  File "/usr/lib/python2.6/ctypes/util.py", line 58, in _get_sonames
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
  File "/usr/lib64/python2.6/subprocess.py", line 642, in __init__
    errread, errwrite)
  File "/usr/lib64/python2.6/subprocess.py", line 1238, in _execute_child
    raise child_exception
OSError: [Errno 2] No such file or directory
</code>
It seems that I'm missing the 'c' library totally, though
