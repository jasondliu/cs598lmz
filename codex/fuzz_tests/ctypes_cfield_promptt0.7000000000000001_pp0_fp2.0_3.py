import ctypes
# Test ctypes.CField
class TestCField:

    def test_is_cfield(self):
        assert isinstance(ctypes.CField, type)

    def test_subclass(self):
        assert issubclass(ctypes.CField, object)

    def test_has_key(self):
        assert hasattr(ctypes.CField, "key")

    def test_has_name(self):
        assert hasattr(ctypes.CField, "name")


class TestCStruct:

    def test_is_cstruct(self):
        assert isinstance(ctypes.CStruct, type)

    def test_subclass(self):
        assert issubclass(ctypes.CStruct, object)

    def test_has_fields(self):
        assert hasattr(ctypes.CStruct, "fields")

    def test_has_name(self):
        assert hasattr(ctypes.CStruct, "name")


class TestCArray:

    def test_is_carray(self):
        assert isinstance(ctypes.CArray, type)

    def test
