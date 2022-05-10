import ctypes
# Test ctypes.CField.from_address() on None.
struct_fake_rffi_bint = lltype.GcStruct('fake_rffi_bint',
                                        ('fake_rffi_bint_val', rffi.INT),
                                        rtti=False)


class A(object):
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return 'A(%d)' % self.i

class B(A):
    def __init__(self, i):
        A.__init__(self, i)

class TestCFieldFromAddress(BaseApiTest):

    def test_cfield_from_address_class_is_none(self):
        # should crash if we pass None to ctypes.CField.from_address()
        # without rpython
        exc_descr_1 = self.get_raises_exception_descr(self.foo, ValueError)
        exc_descr_2 = self.get_raises_exception_descr(self.
