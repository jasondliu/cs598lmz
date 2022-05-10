import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

def test_fun():
    assert fun() == 1
    assert fun.__name__ == 'fun'
    assert fun.__module__ == '__main__'
    assert fun.__doc__ is None

def test_fun_with_doc():
    @FUNTYPE
    def fun():
        '''Doc'''
        return 1
    assert fun() == 1
    assert fun.__name__ == 'fun'
    assert fun.__module__ == '__main__'
    assert fun.__doc__ == 'Doc'

def test_fun_with_name():
    @FUNTYPE
    def fun():
        '''Doc'''
        return 1
    fun.__name__ = 'othername'
    assert fun() == 1
    assert fun.__name__ == 'othername'
    assert fun.__module__ == '__main__'
    assert fun.__doc__ == 'Doc'

def test_fun_with_module():
    @FUNTYPE
    def fun():
        '''Doc'''
        return 1
    fun
