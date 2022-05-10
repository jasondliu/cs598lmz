import ctypes
ctypes.cast(0, ctypes.py_object)
  File "C:\Users\xxx\AppData\Local\Programs\Python\Python35\lib\ctypes\__init__.py", line 361, in cast
    return _simple_cast(obj, typ)
  File "C:\Users\xxx\AppData\Local\Programs\Python\Python35\lib\ctypes\__init__.py", line 324, in _simple_cast
    return obj._as_parameter_
AttributeError: 'int' object has no attribute '_as_parameter_'
</code>
I'm using Pycharm 2017.2.3, using python 3.5 with anaconda 3.6.
Thank you for your help!
UPDATE:
I found the problem. I was trying to import <code>cPickle</code> but I was mixing up <code>c</code> and <code>C</code>. 
<code>cPickle</code> is <code>import cPickle as pickle</code> and <code>ctypes.cast</code> is <code>from ctypes import c_
