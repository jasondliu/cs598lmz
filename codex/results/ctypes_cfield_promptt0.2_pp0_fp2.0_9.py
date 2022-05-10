import ctypes
# Test ctypes.CField
#
# This test is based on the test_ctypes.py test_cfield() test.
#
# The test_cfield() test is a bit confusing.  It tests the
# ctypes.CField class, but it does not test the ctypes.CField
# class directly.  Instead, it tests the ctypes.CField class
# indirectly by testing the ctypes.Structure class.  The
# ctypes.Structure class is a subclass of the ctypes.CField
# class.  The ctypes.Structure class overrides the
# ctypes.CField.__get__() method.  The ctypes.CField.__get__()
# method is called when the ctypes.Structure class is accessed
# as an attribute of an instance of the ctypes.Structure class.
#
# The test_cfield() test creates an instance of the
# ctypes.Structure class.  It then accesses the instance as an
# attribute of the instance.  This causes the ctypes.Structure
# class to call the ctypes.CField.__get__() method.  The
