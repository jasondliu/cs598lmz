import ctypes
# Test ctypes.CFUNCTYPE()
try:
    CFUNCTYPE = ctypes.CFUNCTYPE
except AttributeError:
    pass
else:
    c_string_p = ctypes.c_char_p
    c_int = ctypes.c_int
    c_double = ctypes.c_double
    c_void_p = ctypes.c_void_p
    def echo(s):
        return s
    func = CFUNCTYPE(c_string_p, c_string_p)(echo)
    res = func("Hello")
    assert res == "Hello"
    #
    func2 = CFUNCTYPE(c_double, c_double)(lambda x: x*2)
    res = func2(2.5)
    assert res == 5.0
    #
    def callback1(i, d, s):
        return "%d %f %s" % (i, d, s)
    #
    def callback2(i, d, s):
        return "%d %f %s" % (i*2, d*2,
