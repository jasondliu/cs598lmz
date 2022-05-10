import ctypes
# Test ctypes.CField instance
#
class TestCField:
    def test_subclass(self):
        assert issubclass(ctypes.CField, ctypes.CFuncPtr)

    def test_instance(self):
        assert isinstance(ctypes.CField(), ctypes.CField)

    def test_call(self):
        # The __call__ method is not implemented
        raises(NotImplementedError, ctypes.CField().__call__)

    def test_get_field_type(self):
        # The _get_field_type method is not implemented
        raises(NotImplementedError, ctypes.CField()._get_field_type)
