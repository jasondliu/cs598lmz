import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 23

fun()
</code>
Test code:
<code>import pytest
import ctypes

FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 23

def test_call_fun():
    assert fun() == 23
</code>
Test result with Python 3.6.7:
<code>==================================== test session starts =====================================
platform darwin -- Python 3.6.7, pytest-5.1.1, py-1.8.0, pluggy-0.13.0
rootdir: /Users/hoefling/projects/misc/fun_problem
plugins: cov-2.7.1
collected 1 item                                                                              

test_fun.py .                                                                            [100%]

=================================== 1 passed in 0.01s ====================================
</code>

