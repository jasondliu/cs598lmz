from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(a == b)
print(type(a))
print(type(b))
print(type(a) == type(b))
print(type(a) is type(b))
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))

print(a.gi_code is b.gi_code)
print(a.gi_frame is b.gi_frame)
print(a.gi_frame.f_locals is b.gi_frame.f_locals)

print(a.gi_frame.f_locals)
print(b.gi_frame.f_locals)

print(a.gi_frame.f_locals is b.gi_frame.f_locals)
print(a.gi_code is b.gi_code)
print(a.gi_frame is b.gi_frame)

# 闭包
def count():
    fs = []
    for i in range(1, 4):

