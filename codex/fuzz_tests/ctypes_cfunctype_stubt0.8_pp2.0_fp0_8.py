import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return ''
def f():
    fun()
f()
''')


class AppTestImplicitTyping(AppTestCpythonExtensionBase):
    spaceconfig = dict(usemodules=['struct'])

    def test_short_implicit_conversion(self):
        import struct
        import ctypes
        assert struct.pack("!L", ctypes.c_short(42)) == '*\x00\x00\x00'
        assert struct.pack("<L", ctypes.c_short(42)) == '*\x00\x00\x00'
        assert struct.pack("!L", ctypes.c_ushort(42)) == '*\x00\x00\x00'
        assert struct.pack("<L", ctypes.c_ushort(42)) == '*\x00\x00\x00'

    def test_long_implicit_conversion(self):
        import struct
        import ctypes
        import sys
        assert struct.pack("!Q", ctypes.c_long(42)) == '*' +
