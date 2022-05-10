import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(a):
    """test"""
def test_function(function):
    print(function.__doc__, function() == function.__code__.co_consts[0])
if __name__=="__main__":
    test_function(fun)
