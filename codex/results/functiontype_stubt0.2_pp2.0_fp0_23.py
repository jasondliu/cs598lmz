from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__next__))
print(type(a.__iter__))
print(type(a.send))
print(type(a.throw))
print(type(a.close))
print(type(a.gi_frame))
print(type(a.gi_running))
print(type(a.gi_code))
print(type(a.gi_yieldfrom))

print(type(a.__next__) == FunctionType)
print(type(a.__iter__) == FunctionType)
print(type(a.send) == FunctionType)
print(type(a.throw) == FunctionType)
print(type(a.close) == FunctionType)
print(type(a.gi_frame) == FunctionType)
print(type(a.gi_running) == FunctionType)
print(type(a.gi_code) == FunctionType)
print(type(a.gi_yieldfrom) == FunctionType)

print(a.__next__())
print(a.__next__())


