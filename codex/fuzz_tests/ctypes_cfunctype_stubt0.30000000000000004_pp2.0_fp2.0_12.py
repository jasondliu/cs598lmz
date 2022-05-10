import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

def test_fun():
    assert fun() == "hello"

def test_fun_exception():
    try:
        fun()
    except Exception as e:
        assert "hello" in str(e)

def test_fun_exception2():
    try:
        fun()
    except Exception as e:
        assert "hello" in str(e)
    else:
        assert False


def test_fun_exception3():
    try:
        fun()
    except Exception as e:
        assert "hello" in str(e)
    else:
        assert False
    finally:
        assert True

def test_fun_exception4():
    try:
        fun()
    except Exception as e:
        assert "hello" in str(e)
    else:
        assert False
    finally:
        assert True

def test_fun_exception5():
    try:
        fun()
    except Exception as e:
        assert "hello" in str(e)
    else:
        assert False
   
