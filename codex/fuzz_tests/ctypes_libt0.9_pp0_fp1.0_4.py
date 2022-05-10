import ctypes
ctypes.cdll.LoadLibrary("libmy_own_module.so")
</code>
Assumes that the module is in the current directory.
If you end up compiling a shared library, you don't want to embed the Python API in it, unless you're planning to distribute it separately as a C extension module.  The Python API probably only exists on the build system; <code>pip</code> doesn't bundle the Python API when uploaded to PyPI.

