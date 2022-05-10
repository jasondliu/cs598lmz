import types
types.MethodType

def my_func(self, arg1, arg2):
    print("called my_func with", arg1, arg2)

obj = types.SimpleNamespace()
bound_method = types.MethodType(my_func, obj)
bound_method("arg1", "arg2")

obj.my_method = bound_method
obj.my_method("arg1", "arg2")


# ---
#
#
#
#
#
#
#
