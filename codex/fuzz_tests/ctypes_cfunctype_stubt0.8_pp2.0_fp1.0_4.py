import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 0

@FUNTYPE
def fun2():
    return 0

fun2.__module__ = 'foo'
fun2.__name__ = 'baz'

@nottest
def test_error():
    # Creating a new PyFunction object with builtins=None, globals=None,
    # and code=None is not valid, and should raise a TypeError.
    with assert_raises(TypeError):
        PyFunction(None, None, None)

def test_junk_builtins():
    # Ensure we don't crash when the builtins are not a dict
    with assert_raises(TypeError):
        function_code(None, None, None)

def test_attr_error():
    # Ensure we don't crash when the builtins dict doesn't have a __name__
    # attribute that is a string
    with assert_raises(AttributeError):
        function_code({}, None, None)

def test_module_name_must_be_string():
    # Ensure we don't crash when the builtins dict has a __name__ attribute
