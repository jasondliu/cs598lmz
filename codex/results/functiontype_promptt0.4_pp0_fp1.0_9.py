import types
# Test types.FunctionType
def test_types_FunctionType():
    assert isinstance(test_types_FunctionType, types.FunctionType)

# Test types.GeneratorType
def test_types_GeneratorType():
    def generator():
        yield 1
    assert isinstance(generator(), types.GeneratorType)

# Test types.GetSetDescriptorType
class TestClass:
    def __get__(self, obj, objtype):
        return 1
    def __set__(self, obj, value):
        pass
    def __delete__(self, obj):
        pass
class TestClass2:
    def __get__(self, obj, objtype):
        return 1
    def __set__(self, obj, value):
        pass
    def __delete__(self, obj):
        pass
    def __getattribute__(self, name):
        pass
class TestClass3:
    def __get__(self, obj, objtype):
        return 1
    def __set__(self, obj, value):
        pass
    def __delete__(self, obj):
