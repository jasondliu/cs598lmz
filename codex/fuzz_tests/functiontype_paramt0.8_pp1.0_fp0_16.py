from types import FunctionType
list(FunctionType(s, globals(), "foo") for s in ("pass", "pass", "pass"))

# help and dir
def f():
    pass
f.__help__ = "help"
f.__dir__ = dir
f.__name__ = "f"
f.__module__ = ""
result = [x for x in dir(f)]
expected = ["__call__", "__class__", "__closure__", "__code__", "__defaults__",
            "__delattr__", "__dir__", "__doc__", "__eq__", "__format__",
            "__ge__", "__get__", "__getattribute__", "__gt__", "__hash__",
            "__help__", "__init__", "__le__", "__lt__", "__module__", "__name__",
            "__ne__", "__new__", "__qualname__", "__reduce__", "__reduce_ex__",
            "__repr__", "__setattr__", "__sizeof__", "__str__",
