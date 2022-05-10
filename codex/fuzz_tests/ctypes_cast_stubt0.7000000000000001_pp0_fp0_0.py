import ctypes
ctypes.cast(m, ctypes.py_object).value = 'a'
</code>
I suspect this is the closest you'll get to a 'good' solution, although I'm not sure why you would want to do this.

