import types
types.MethodType(func, obj)  # create a bound method from `func`

# unbound methods can be converted to functions using `__func__`
unbound.__func__(obj, *args)  # call the underlying function

# bound methods can be converted to functions using `__func__`
unbound.__func__(obj, *args)  # call the underlying function
