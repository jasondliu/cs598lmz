import weakref
# Test weakref.ref class
# Refer to:
# http://docs.python.org/lib/typeweakref.html
# https://docs.python.org/3/library/weakref.html

def weakref_array():
    print('Testing weakref.ref and weakref.proxy')
    try:
        a = u64_array([1, 2, 3, 4])
        # weakref.ref(a)
        r1 = weakref.ref(a)
        r2 = weakref.ref(a)

        print(r1)
        print(r2)
        print(r1().ctypes.data)
        assert r1 is r2
        a.append(100)
        assert r1().shape == u64_array([5]).shape
        assert r1().ctypes.data == r2().ctypes.data
        print('a =', a.ctypes.data)
        print('r =', r1().ctypes.data)

        a = None
        print('a =', a)
        print('r =', r1())
        assert r1() is
