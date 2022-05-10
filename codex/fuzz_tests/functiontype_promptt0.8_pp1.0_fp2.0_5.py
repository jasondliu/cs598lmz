import types
# Test types.FunctionType, types.ClassType
def func(a, b=None, *args, **kwargs): pass
class cls: pass

assert_raises(TypeError, types.FunctionType, func)
assert_raises(TypeError, types.FunctionType, func, {}, {})
assert_raises(TypeError, types.FunctionType, func, None, {})
assert_raises(TypeError, types.FunctionType, func, "abc")
assert_raises(TypeError, types.FunctionType, func, "", {})
assert_raises(TypeError, types.FunctionType, func, {}, {}, ("a", "b"), ("c", ))
assert_raises(TypeError, types.FunctionType, func, {}, {}, ("a", "b"))
assert_raises(TypeError, types.FunctionType, func, {}, {}, (1,))
assert_raises(TypeError, types.FunctionType, func, {}, {}, (), ("c",))
assert_raises(TypeError, types.FunctionType, func, {}, {}, (), ("c", "
