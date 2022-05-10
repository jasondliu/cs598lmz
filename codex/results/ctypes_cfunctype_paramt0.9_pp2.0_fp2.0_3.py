import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None)
def assemble_function(x86_64i, nargs):
    code_bytes = bytearray(x86_64i, 'utf-8')
    # print(code_bytes, len(code_bytes))
    ptr = ctypes.cast(ctypes.create_string_buffer(code_bytes), ctypes.c_void_p).value
    # print(ptr)
    return FUNTYPE(ptr)
def make_python_callable(f):
    c_nargs = ctypes.c_int(nargs)
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        # print(c_nargs, '*args', *args, '**kwargs', **kwargs)
        return f(c_nargs, *args, **kwargs)
    return wrapper
#########################################

# In[3]:


from pycparser import c_parser, c_ast, c_generator

class FunctionCallVisitor(c_ast.NodeVisitor):
    def __init__(self, function
