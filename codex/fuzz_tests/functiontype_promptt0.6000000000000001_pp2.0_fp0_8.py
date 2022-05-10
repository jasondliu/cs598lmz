import types
# Test types.FunctionType

def test_function_type():
    def f():
        pass

    assert isinstance(f, types.FunctionType)

def test_instance_method_type():
    class C(object):
        def f(self):
            pass

    assert isinstance(C.f, types.FunctionType)

def test_unbound_method_type():
    class C(object):
        def f(self):
            pass

    assert isinstance(C().f, types.MethodType)

def test_builtin_function_type():
    assert isinstance(list, types.BuiltinFunctionType)

def test_builtin_method_type():
    assert isinstance(list.append, types.BuiltinMethodType)

def test_lambda_type():
    l = lambda : None

    assert isinstance(l, types.LambdaType)

def test_method_descriptor_type():
    assert isinstance(dict.__dict__['copy'], types.MethodDescriptorType)

def test_method_wrapper_type():
    assert is
