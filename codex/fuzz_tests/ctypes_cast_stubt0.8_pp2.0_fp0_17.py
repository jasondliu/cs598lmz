import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
It gives a "WindowsError: exception: access violation" exception.
I can call <code>cast()</code> with any other address (not 0) and it doesn't fail.
Can anyone explain why this happens?
Running on Windows 8.1, Python 2.7.9.

