import ctypes
ctypes.cast(0, ctypes.py_object)

def test_cast_from_integer():
    # ctypes.cast(int, ctypes.py_object)
    raises(TypeError, ctypes.cast, 0, ctypes.py_object)

def test_cast_from_string():
    # ctypes.cast(str, ctypes.py_object)
    raises(TypeError, ctypes.cast, "", ctypes.py_object)

def test_cast_from_unicode():
    # ctypes.cast(unicode, ctypes.py_object)
    raises(TypeError, ctypes.cast, u"", ctypes.py_object)

def test_cast_from_float():
    # ctypes.cast(float, ctypes.py_object)
    raises(TypeError, ctypes.cast, 0.0, ctypes.py_object)

def test_cast_from_instance():
    # ctypes.cast(instance, ctypes.py_object)
    raises(TypeError, ctypes.cast, object(), ctypes.
