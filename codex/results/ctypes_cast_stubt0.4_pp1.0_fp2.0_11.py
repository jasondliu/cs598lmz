import ctypes
ctypes.cast(0, ctypes.py_object).value

# Out[11]: 0

# In[12]:

# ctypes.cast(0, ctypes.py_object).value = 1

# Out[12]:

# ---------------------------------------------------------------------------

# AttributeError                            Traceback (most recent call last)

# <ipython-input-12-01d8f7c2a9b9> in <module>()
# ----> 1 ctypes.cast(0, ctypes.py_object).value = 1

# AttributeError: 'int' object has no attribute 'value'

# In[13]:

import ctypes
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]

class PyIntObject(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_long),
                ("ob_type", ctypes.c_void_p),
                ("ob_size", ctypes.c_long),
                ("ob_digit", ctypes
