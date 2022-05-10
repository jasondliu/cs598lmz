import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def test_build_function_type():
    # test that we can build a simple function type
    Bool = gdb.lookup_type("bool")
    Func = gdb.lookup_type("int").pointer()
    int_func_ptr = gdb.lookup_type("int").pointer().pointer()
    FuncType = gdb.lookup_type("int").function_type(Bool, Func, int_func_ptr)
    assert FuncType.code == gdb.TYPE_CODE_FUNC
    assert FuncType.name == 'int(bool, int *, int(**)(int))'
    assert FuncType.tag == None
    assert FuncType.target() == gdb.lookup_type("int")
    assert FuncType.fields()[0].name == 'arg0'
    assert FuncType.fields()[0].type == Bool
    assert FuncType.fields()[1].name == 'arg1'
    assert FuncType.
