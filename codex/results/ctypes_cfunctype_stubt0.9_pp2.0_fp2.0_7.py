import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

# Get an annotated C error value
def get_error(space):
    return OperationError(space.w_RuntimeError, space.wrap("nop"))
op_direct = Gateway((
    dict( name = "direct_function",
          m_returns = PyObjectType,
          c_returns = PyObjectType,
          code = r"""
     if (PyCallable_Check(args)) 
         return PyObject_Call(args, args2, NULL);
     else {
         PyErr_SetString(PyExc_RuntimeError, "non-callable object");
         return NULL;
     }
"""),),
                    gateway, # supplying the Gateway instance
                    get_error, # supplying the function that returns
                               # an annotated C error value
                    )
print op_direct.c_decl(["callable"])

def callable(o):
    return op_direct.callable(o)

assert callable(fun()) is None


class W_Object1(W_Root):
    pass
class W_Object2(W
