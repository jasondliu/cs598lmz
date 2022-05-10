import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

class AppTestCallable:
    def test_callable(self):
        assert callable(len)
        assert not callable(len([]))
        assert callable(callable)
        assert callable(lambda x: x)
        assert callable(self.test_callable)
        assert callable(int)
        assert not callable(1)
        assert not callable(1.0)
        assert not callable(object)
        assert not callable(1j)
        assert not callable(None)
        assert not callable("")
        assert not callable(u"")
        assert not callable(b"")
        assert not callable(bytearray(b""))
        assert not callable(range(0))
        assert not callable(True)
        assert not callable(False)
        assert not callable(Ellipsis)
        assert not callable(NotImplemented)
        assert not callable(slice(0))
        assert not callable(x for x in range(0))
        assert not call
