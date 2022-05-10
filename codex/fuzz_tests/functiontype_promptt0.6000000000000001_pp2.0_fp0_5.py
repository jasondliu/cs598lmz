import types
# Test types.FunctionType
def test_function_type():
    def func():
        pass
    assert isinstance(func, types.FunctionType)

# Test types.GeneratorType
def test_generator_type():
    def generator():
        yield 1
    g = generator()
    assert isinstance(g, types.GeneratorType)

# Test types.GetSetDescriptorType
# TODO: not implemented
#def test_getset_descriptor_type():
#    pass

# Test types.LambdaType
def test_lambda_type():
    l = lambda x: x
    assert isinstance(l, types.LambdaType)

# Test types.MappingProxyType
# TODO: not implemented
#def test_mapping_proxy_type():
#    pass

# Test types.MemberDescriptorType
# TODO: not implemented
#def test_member_descriptor_type():
#    pass

# Test types.MethodType
# TODO: not implemented
#def test_method_type():
#    pass

# Test types
