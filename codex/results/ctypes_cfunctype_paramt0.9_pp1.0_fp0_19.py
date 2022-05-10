import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int)
undefined_function = FUNTYPE(undefined_function)
</code>
The <code>cfuntotype</code> function allows you to import a function from your dll as a python callable and then you can use it just like <code>ctypes.CDLL.getattr</code> does.

