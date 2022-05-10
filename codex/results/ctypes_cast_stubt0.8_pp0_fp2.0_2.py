import ctypes
ctypes.cast(0, ctypes.py_object)
</code>
Python 2.6 returns the raw int, which is then downgraded to str.
<code>PyObject *int0 = PyInt_FromLong(0);
</code>
But Python 2.7 returns PyLongObject:
<code>PyObject *int0 = _PyLong_FromLong(0);
</code>
The former is castable to <code>PyStringObject</code>, but not the latter I guess.
Is there a work-around? We are running on Windows, so <code>ctypes.cast</code> does not seem to be an option...
Edit: After studying the Python source code for a while, there does not seem to be any distinction between <code>PyLongObject</code> and <code>PyIntObject</code> at all. I am still baffled as to why it returns <code>PyLongObject</code> in the first place - could it have something to do with the fact that we are calling <code>PyRun_SimpleStringFlags</code> in a non-zero thread?

