import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class AppTestPyslices:
    def test_slice_assign(self):
        a = []
        a[:] = [1,2,3,4]
        assert a == [1,2,3,4]

    def test_slice_assign_slice(self):
        a = [1,2,3,4,5,6]
        a[1:3] = [7,8]
        assert a == [1,7,8,4,5,6]

    def test_slice_assign_slice_from_empty(self):
        a = []
        a[1:3] = [7,8]
        assert a == [7,8]

    def test_slice_assign_to_slice(self):
        a = [1,2,3,4,5,6]
        a[1:3] = [9,9,9,9,9]
        assert a == [1,9,9,9,9,9,4,5,6]

    def test_slice_assign
