import select

def test_select_mutated():
    a = []

    class F:
        def fileno(self):
            test_select_mutated()
            return -1
        def read(self):
            test_select_mutated()
            a[:] = 1 # Force a list grow
    f = F()

    def callback(*args):
        raise ValueError # prevent entering infinite recursion

    for i in range(5):
        try:
            select.select([f], [], [], -1.0, callback)
        except:
            pass


# Test handling of math.errno with select.select
try:
    import math
    def setsimulateerrno(n):
        math.errno = n

    def callback(*args):
        raise ValueError

    select.select([], [], [], -1.0, callback)
except:
    pass


# Test passing ctypes.Structure into select
try:
    import ctypes

    class TestStructure(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]

    test = TestStructure()
    test.a = 1

    def setsimulateerrno(n):
        test.a = n
