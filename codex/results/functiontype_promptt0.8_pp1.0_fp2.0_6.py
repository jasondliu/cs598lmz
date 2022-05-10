import types
# Test types.FunctionType
def test_function_type():
    def foo(): pass
    def bar(a, b): pass
    def baz(a, b, *args): pass
    def spam(a, b, c=5, d=0): pass
    def grok(a, b, *args, **kwargs): pass
    def m1(a, b, *, c, **kwargs): pass

    if verbose:
        print("testing FunctionType")
    assert type(foo) is types.FunctionType, \
           'function type is not FunctionType'
    assert type(bar) is types.FunctionType, \
           'function type is not FunctionType'
    assert type(baz) is types.FunctionType, \
           'function type is not FunctionType'
    assert type(spam) is types.FunctionType, \
           'function type is not FunctionType'
    assert type(grok) is types.FunctionType, \
           'function type is not FunctionType'
    assert type(m1) is types.FunctionType, \
           'function type is not FunctionType'
