import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    """test"""
    yield (1,2)
    lst = ctypes.py_object()
    lst.append(1)
    
@FUNTYPE
def fun(a):
    """test"""
    return a

def test_function(function):
    """
    <<real_function>>() : <<value>>
    """
    print(function.__doc__, function() == function.__code__.co_consts[0])

if __name__=="__main__":
    test_function(fun)
