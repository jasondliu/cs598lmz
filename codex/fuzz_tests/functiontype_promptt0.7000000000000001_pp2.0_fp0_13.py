import types
# Test types.FunctionType
def test_function_type():
    def a():
        pass
    assert type(a) == types.FunctionType
    a()

test_function_type()

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert type(len) == types.BuiltinFunctionType

test_builtin_function_type()

# Test types.ModuleType
def test_module_type():
    assert type(types) == types.ModuleType
    assert type(sys) == types.ModuleType

test_module_type()

# Test types.FileType
def test_file_type():
    assert type(sys.stderr) == types.FileType

test_file_type()

# Test types.MethodType
def test_method_type():
    assert type(sys.stderr.write) == types.MethodType
    class A(object):
        def a(self):
            pass
    a = A()
    assert type(a.a) == types.MethodType

test_method_type()


