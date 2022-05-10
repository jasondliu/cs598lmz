import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A:
    def m2(self):
        return 2

class B(A):
    def m1(self):
        return 1

class C(A):
    def m3(self):
        return 3
    def m1(self):
        return 4

class D(B, C):
    pass

d = D()

testclasses = {
    'mro_test1': D,
    'mro_test2': B,
    'mro_test3': C,
    'mro_test4': A,
    'mro': [B, C, A, object],
    'mro_test': [D, B, C, A, object],
    'mro_test5': [A, object],
    'cfield': S.x,
}

if __name__ == '__main__':
    import __builtin__
    mod = sys.modules[__name__]
    for k, v in testclasses.items():
        __builtin__.__dict__[k] = v
       
