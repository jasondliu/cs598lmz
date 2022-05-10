import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

def test_non_sequence_with_len():
    class A:
        def __init__(self):
            self.x = 1
            self.y = 2
        def __len__(self):
            return 2
    a = A()
    assert list(a) == [1, 2]

def test_slice_index():
    class A:     pass
    class B(A):  pass
    class C(A):  pass
    class D(C):  pass
    class E(D):  pass
    class F(E):  pass
    class G(F):  pass

    def listify(t):
        return list(t)

    def get_elements(t, i):
        return t[i]

    def slice_tuple(t, i):
        return t[i:]

    def slice_list(t, i):
        return t[i:]

    def slice_array(t, i):
        return t[i:]

    def slice_recursive(t, i):
        return t[i:]


