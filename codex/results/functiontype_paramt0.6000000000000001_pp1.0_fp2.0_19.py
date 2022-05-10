from types import FunctionType
list(FunctionType('f', globals(), None, None, None) for f in [f1, f2])

# f1.__closure__ = (c1,)
# f2.__closure__ = (c2,)

# for i in range(2):
#     d = {'x': i}
#     exec(f1.__code__, d)
#     print(d['x'])

# for i in range(2):
#     d = {'x': i}
#     exec(f2.__code__, d)
#     print(d['x'])

# print(f1.__code__.co_freevars)
# print(f2.__code__.co_freevars)
