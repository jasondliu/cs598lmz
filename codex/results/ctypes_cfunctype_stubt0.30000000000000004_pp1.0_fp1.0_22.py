import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_with_arg():
    assert fun(1) == "hello"
</code>
I get the following error:
<code>$ pytest test_fun.py
============================= test session starts ==============================
platform linux -- Python 3.6.3, pytest-3.2.5, py-1.5.2, pluggy-0.4.0
rootdir: /home/user/test, inifile:
collected 2 items

test_fun.py F                                                              [100%]

================================== FAILURES ===================================
________________________________ test_fun_with_arg _______________________________

    def test_fun_with_arg():
&gt;       assert fun(1) == "hello"
E       TypeError: fun() takes 0 positional arguments but 1 was given

test_fun.py:11: TypeError
=========================== short test summary info ============================
FAILED test_fun.py::test_fun_with_arg - TypeError: fun()
