import ctypes
ctypes.cast(123, ctypes.py_object)

#pylint: disable=pointless-statement
ctypes.cast(123, ctypes.py_object);

#pylint: disable=expression-not-assigned
ctypes.cast(123, ctypes.py_object)

#pylint: disable=assignment-from-none
_ = ctypes.cast(123, ctypes.py_object)
