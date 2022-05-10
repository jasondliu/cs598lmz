import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CField_Test(unittest.TestCase):
    def test(self):
        # doctest not working on IronPython
        import os
        if os.name == "nt":
            # COM class not registered on Win64,
            # _ctypes.COMError: (-2147221164, 'Class not registered', None, None)
            return

        for ob_type, expected in [
                (ctypes.Field, str("Field_Type(names=[], fields=(), pack=0)")),
                (ctypes.Struct, str("Struct_Type(names=[], fields=(), pack=0)")),
                (ctypes.Array, str("Array_Type(None, None)")),
                (ctypes.Union, str("Union_Type(names=[], fields=(), pack=0)")),
                (ctypes.CFuncPtr, str("CFuncPtrType(None, None)")),
                (ctypes.POINTER, str("PointerType(None)")),
                (ctypes.c_int, str("c_int")),
               
