import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_type():
    assert type(fun) is FUNTYPE

def test_fun_type_type():
    assert type(type(fun)) is type

def test_fun_type_type_type():
    assert type(type(type(fun))) is type

def test_fun_type_type_type_type():
    assert type(type(type(type(fun)))) is type
</code>
Which gives:
<code>$ py.test test_fun.py
============================= test session starts ==============================
platform darwin -- Python 2.7.5 -- pytest-2.3.4
plugins: cov
collected 6 items 

test_fun.py ...

========================== 6 passed in 0.01 seconds ===========================
</code>

