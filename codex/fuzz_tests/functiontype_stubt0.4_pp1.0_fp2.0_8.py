from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x: x for x in [1]}
e = FunctionType(lambda: None, {})
f = lambda: None
g = type(lambda: None)
h = type(type(lambda: None))
i = type(FunctionType(lambda: None, {}))
j = type(type(FunctionType(lambda: None, {})))
k = type(type(type(FunctionType(lambda: None, {}))))
l = type(type(type(type(FunctionType(lambda: None, {})))))
m = type(type(type(type(type(FunctionType(lambda: None, {}))))))
n = type(type(type(type(type(type(FunctionType(lambda: None, {})))))))
o = type(type(type(type(type(type(type(FunctionType(lambda: None, {}))))))))
p = type(type(type(type(type(type(type(type(FunctionType(lambda: None, {})))))))))
q = type(type(type
