import ctypes
ctypes.cast(0, ctypes.py_object)

class PythonAPITest(unittest.TestCase):
    """Test the Python C API"""

    def test_string_from_format(self):
        msg = "hello %s"
        args = ("world",)
        s = ctypes.pythonapi.PyString_FromFormat
        s.restype = ctypes.py_object
        self.assertEqual(s(msg, *args), "hello world")

    def test_string_from_string_and_size(self):
        buf = "hello world"
        s = ctypes.pythonapi.PyString_FromStringAndSize
        s.restype = ctypes.py_object
        self.assertEqual(s(buf, len(buf)), buf)

    def test_pyobject_getattrstring(self):
        import sys

        s = ctypes.pythonapi.PyObject_GetAttrString
        s.restype = ctypes.py_object
        s.argtypes = ctypes.py_object, ctypes.c_char_p

       
