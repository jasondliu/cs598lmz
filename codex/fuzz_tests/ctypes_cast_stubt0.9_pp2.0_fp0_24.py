import ctypes
ctypes.cast(array.ctypes.data, ctypes.c_void_p)
</code>
But for some reason it does not work for <code>webbrowser</code> and <code>http.client</code>.
<code>from numpy.ctypeslib import as_ctypes
from ctypes import c_void_p
from http.client import HTTPConnection
from webbrowser import open as open_webpage

a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)

ctypes.cast(a.ctypes.data, c_void_p)  # works
ctypes.cast(np.ctypeslib.as_ctypes(a)._objects[0], c_void_p)  # works

ctypes.cast(np.ctypeslib.as_ctypes(a)._objects[0], c_void_p)  # works
ctypes.cast(as_ctypes(a)._objects[0], c_void_p)  # doesn't work for some reason

HTTPConnection.connect(
