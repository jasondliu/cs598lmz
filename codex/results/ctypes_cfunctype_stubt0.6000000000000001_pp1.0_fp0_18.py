import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

def f():
    return fun()

class AppTest(object):
    spaceconfig = {'objspace.std.withmultiphase': True}

    def setup_class(cls):
        if cls.runappdirect:
            py.test.skip("can't run appdirect with multiphase")
        cls.w_runappdirect = cls.space.wrap(cls.runappdirect)
        cls.w_has_threads = cls.space.wrap(hasattr(sys, 'getcheckinterval'))

    def test_get_type(self):
        assert fun.__class__ is types.FunctionType
        assert fun.__name__ == 'fun'
        assert fun.__doc__ is None
        assert fun.__dict__ == {}
        assert fun.__module__ == '__main__'
        assert fun.__code__.co_argcount == 0
        assert fun.__defaults__ == ()
        assert fun.__closure__ is None
        assert fun.__annotations__ == {}
       
