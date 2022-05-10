import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return range(10)

def _cfun():
    return fun()

def test_cfunc():
    """
    >>> test_cfunc()
    True
    """
    return list(_cfun()) == range(10)

def test_function_addr():
    """
    >>> test_function_addr()
    True
    """
    return hex(_cfun.func_code.co_code) == '0xdeadbeef'

def test_function_addr_cached():
    """
    >>> test_function_addr_cached()
    True
    """
    return hex(_cfun.func_code.co_code) == hex(_cfun.func_code.co_code)

def test_function_addr_changes_when_uncompiled():
    """
    >>> test_function_addr_changes_when_uncompiled()
    True
    """
    return hex(_cfun.func_code.co_code) != hex(pyjitpl_compile_and_run(_cfun).func_code.co_code)

