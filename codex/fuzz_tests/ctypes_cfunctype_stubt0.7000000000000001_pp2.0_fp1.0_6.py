import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_non_python_calls():
    # this test is for an obscure corner case
    # of the ctypes bridge: if you have a ctypes
    # object which returns a non-python object,
    # and you pass it to a different thread, then
    # the second thread will see a non-python object
    # and it will need to convert it to a python object.
    # However, if the object was produced by a different
    # thread, then the "conversion" will fail, because
    # it cannot access the array of function pointers.
    # (the array of function pointers is thread-local)
    #
    # This test is a regression test for a bug that
    # was happening in the ctypes bridge: the ctypes
    # bridge would crash when trying to access the
    # array of function pointers.
    t = threading.Thread(target=fun)
    t.start()
    t.join()
    assert t.result == "hello"


def test_return_value_of_None():
    # Test return value of None
