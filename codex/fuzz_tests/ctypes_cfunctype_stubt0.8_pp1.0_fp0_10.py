import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@njit
def test():
    return fun()

test()
 
# Reconstruction
def test_reconstruction():
    funs = {
        test : """
            def f(x):
                return fun()
            return f(x)
        """,
    }
    for fun, expected in funs.items():
        assert inline_func(fun).strip() == expected.strip()

#############################################################################
# Util

def _eq(tree, expect):
    from textwrap import dedent
    from numba.core.compiler import compile_extra

    cres = compile_extra(tree, (types.int32,), backend='ast')

    ast_str = asdl.format_module(cres.signature.return_type.asdl_code)
    ast_str = ast_str.replace("Assign(targets=[Name(id='result', ctx=Store())], value=",
                              "Assign(targets=[Name(id='result', ctx=Store())], value=Const(value="
