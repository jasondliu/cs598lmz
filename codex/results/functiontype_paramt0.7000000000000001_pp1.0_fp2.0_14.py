from types import FunctionType
list(FunctionType(lambda: None, globals()))
assert_equal(list, [])

# instance method
list(type.__dict__["mro"].__get__([], type))
assert_equal(list, [type.__dict__["mro"].__get__([], type)])
