import types
# Test types.FunctionType
def test_FunctionType():
    def f(): pass
    assert isinstance(f, types.FunctionType)
    assert isinstance(test_FunctionType, types.FunctionType)
    class X(object):
        def g(self): pass
    assert isinstance(X.g, types.FunctionType)
    assert isinstance(X.__init__, types.FunctionType)
    assert isinstance(X.__new__, types.FunctionType)
    assert isinstance(X.__del__, types.FunctionType)
    assert isinstance(X.__repr__, types.FunctionType)
    assert isinstance(X.__str__, types.FunctionType)
    assert isinstance(X.__getattribute__, types.FunctionType)
    assert isinstance(X.__setattr__, types.FunctionType)
    assert isinstance(X.__delattr__, types.FunctionType)
    assert isinstance(X.__hash__, types.FunctionType)
    assert isinstance(X.__cmp__, types.FunctionType)
    assert isinstance(X.__
