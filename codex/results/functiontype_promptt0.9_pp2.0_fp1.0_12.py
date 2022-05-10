import types
# Test types.FunctionType
def test_func(x,y):
    return x + y
assert isinstance(test_func, types.FunctionType)
assert str(types.FunctionType) == "<class 'function'>"

print ("FunctionType tests passed!")

# Test types.MethodType
class myclass(object):
    def myfunc(self):
        assert isinstance(self, myclass)
test_obj = myclass()
test_boundmethod = test_obj.myfunc
assert(isinstance(test_boundmethod, types.MethodType))
assert str(types.MethodType) == "<class 'instancemethod'>"

print ("MethodType tests passed!")

# Test types.GeneratorType
def mygen():
    i = 1
    yield i
for i in mygen():
    assert(isinstance(i, types.GeneratorType)==False)
gen_obj = mygen()
assert(isinstance(gen_obj, types.GeneratorType))
assert str(types.GeneratorType) == "<class 'generator'>"

print ("GeneratorType tests passed!")

