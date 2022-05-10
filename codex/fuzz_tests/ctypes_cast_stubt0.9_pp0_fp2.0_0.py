import ctypes
ctypes.cast(digester, ctypes.py_object).value = digester
</code>
This is all assuming that your <code>digest</code> function doesn't need to be called from multiple threads simultaneously, since <code>digester</code> isn't thread-local.

