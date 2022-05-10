from types import FunctionType
a = (x for x in [1])
print("type(a) = %s" % type(a))
print("type(type(a)) = %s" % type(type(a)))
print("isinstance(a,FunctionType) = %s" % isinstance(a,FunctionType))
