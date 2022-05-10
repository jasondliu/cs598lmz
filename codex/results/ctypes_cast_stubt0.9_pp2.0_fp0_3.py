import ctypes
ctypes.cast(None, ctypes.py_object)
import numpy
numpy.zeros(5)
import ssl
ssl.OP_NO_TICKET
import socket
socket.gethostname()
</code>
Run it and you get a warning message:
<code>Warning (from warnings module):
  File "C:\Users\***\AppData\Roaming\Python\Python36\site-packages\IPython\extensions\rmagic.py", line 14
    from rpy2.robjects.robject import RObjectMixin, RObject
DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
This application is using an unsupported version of pyreadline 2.0 (2.1 is supported).  pyreadline 2.0 is no longer developed or maintained and is only kept for backwards compatibility.  You should upgrade to 2.1+.

In [1]:
</code>
Notice that the warning is from the module <code>ipython.extensions.rmagic</code>.
This is because the first non-code line <code>%load_ext r
