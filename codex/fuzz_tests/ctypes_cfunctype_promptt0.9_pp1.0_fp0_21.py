import ctypes
# Test ctypes.CFUNCTYPE
import ctypes
import platform


class test_pythonapi(unittest.TestCase):
    def test_CFUNCTYPE(self):
        # PyPy doesn't allow to create forward declarations of callbacks
        # with None result type.
        if platform.python_implementation() == 'PyPy':
            with self.assertRaises(TypeError):
                # This used to segfault when compiled on older PyPy versions.
                ret = ctypes.CFUNCTYPE(None, ctypes.py_object)
            return

        # argument types can be ctypes classes, ctypes instances or None.
        cb = ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
        cb = ctypes.CFUNCTYPE(ctypes.py_object, None)

        # If no argument or result types are given, the type is
        # int(*)() or void(*)() depending on whether or not restype is given.
        cb = ctypes.CFUNCTYPE()
        self.assertEqual(
