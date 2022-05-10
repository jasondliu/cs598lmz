import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello world'

def test_funcall_allowed():
    '''
    funcall is allowed
    '''
    assert fun() == 'hello world'

def test_simple_funcall_allowed():
    '''
    simple funcall is allowed
    '''
    assert fun.__simple_funcall__() == 'hello world'

def test_funcall_allowed_factory():
    '''
    funcall is allowed using funcall factory
    '''
    assert fun.__funcall__() == 'hello world'

def test_getitem_allowed():
    '''
    getitem is allowed
    '''
    assert fun['hello'] == 'hello world'

def test_simple_getitem_allowed():
    '''
    simple getitem is allowed
    '''
    assert fun.__simple_getitem__('hello') == 'hello world'

def test_getitem_allowed_factory():
    '''
    getitem is allowed using getitem factory
    '''
    assert fun.__getitem__('hello')
