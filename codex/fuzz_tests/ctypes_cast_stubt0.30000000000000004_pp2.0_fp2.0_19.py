import ctypes
ctypes.cast(0, ctypes.py_object)

# This is a hack to force the object mode runtime to be loaded,
# otherwise the test_ctypes test fails.
import _ctypes

# This is a hack to force the object mode runtime to be loaded,
# otherwise the test_ctypes test fails.
import _rawffi

class AppTestCtypes:
    spaceconfig = dict(usemodules=['_rawffi', 'itertools'])

    def setup_class(cls):
        cls.w_runappdirect = cls.space.wrap(option.runappdirect)
        cls.w_runappdirect_tmp = cls.space.wrap(option.runappdirect_tmp)
        cls.w_lib_name = cls.space.wrap(str(udir.join('test_ctypes.so')))

    def test_simple(self):
        import _ctypes
        raises(AttributeError, "ctypes.Structure.foo")
        raises(AttributeError, "ctypes.Structure.__dict__")
        raises(Attribute
