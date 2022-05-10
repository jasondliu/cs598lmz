import ctypes
# Test ctypes.CField
# <https://github.com/lemon24/python-ctypes/blob/master/docs/specification/ctypes_specification.rst#cfield>

import ctypes

class TestCField:
    class TestAllocation:
        def test_in_ctype(self):
            # Test that p_type is allocated in the ctypes module.
            assert hasattr(ctypes, 'p_int')

        def test_in_ctypes(self):
            # Test that p_type is exposed in the ctypes module.
            assert type(ctypes.p_int) is ctypes._pointer_t

        def test_in_types(self):
            # Test that p_type is allocated in the types module.
            import types
            assert type(types.p_int) is ctypes._pointer_t

    class TestInheritance:
        def test_inherits_from_ctypes_CFuncPtr(self):
            # Test that p_type inherits from ctypes._CFuncPtr.
            class FakeCFunctionType(ctypes._CFuncPtr
