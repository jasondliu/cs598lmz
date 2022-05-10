import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Mixed arguments"

def fun():
    return "No arguments"

def fun():
    return "Fixed arguments", "hello"

def fun(arg1, arg2, **args):
    return "Keyword arguments"

def fun(arg1, *args, **kwargs):
    return "Mixed arguments"
class TestBasic:
    @pytest.mark.skip(reason='')
    def test_init_repr_call_invalid_args(self):
        d = _testcapi.PyCFunction_New(myfunctype, _testcapi.test_struct)
        # This won't raise an exception: the C-API docs are wrong.
        # It turns out that you can only get an exception if there
        # is no __call__ method object in the PyCFunctionObject
        # (i.e. it only happens for built-in functions).
        # This is because the check in PyObject_Call() relies on
        # m_meth->ml_meth (as opposed to m_self).
        # self.assertRa
