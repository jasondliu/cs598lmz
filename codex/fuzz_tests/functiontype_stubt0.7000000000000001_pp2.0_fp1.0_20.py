from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a.gi_code == b.gi_code)
print(a.gi_frame == b.gi_frame)
print(a.gi_frame.f_globals == b.gi_frame.f_globals)
print(a.gi_frame.f_locals is b.gi_frame.f_locals)

# print(isinstance(a, FunctionType))
a = 1
b = 1
print(a == b)


def a():
    pass
a = a
print(a is a)

a = [1]
b = [1]
print(a == b)
print(a is b)
print(a[0] is b[0])

a = (1,)
b = (1,)
print(a == b)
print(a is b)
print(a[0] is b[0])

# a = {1}
# b = {1}
# print(a == b)
# print(a is b)
# print(a[
