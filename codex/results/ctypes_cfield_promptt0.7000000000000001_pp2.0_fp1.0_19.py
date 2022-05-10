import ctypes
# Test ctypes.CField


class TestCField:

    def setup_method(self):
        self.fieldtype = ctypes.c_uint
        self.fieldname = "foo"
        self.field = ctypes.CField(self.fieldtype, self.fieldname)
        self.field.from_address = lambda x: 1
        self.field.offset = 0

    def test_type(self):
        assert self.field.type is self.fieldtype

    def test_name(self):
        assert self.field.name == self.fieldname

    def test_read(self):
        assert self.field.read(None) == 1


# Test ctypes.CStruct


class TestCStruct:

    def setup_method(self):
        self.fieldtype = ctypes.c_uint
        self.fieldname = "foo"
        self.field = ctypes.CField(self.fieldtype, self.fieldname)
        self.field.from_address = lambda x: 1

        self.struct = ctypes.CStruct("foo_t", [self.field])


