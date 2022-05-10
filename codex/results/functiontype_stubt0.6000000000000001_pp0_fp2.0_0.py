from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(isinstance(a, FunctionType))
print(a == b)
print(a is b)
print(a.gi_frame is b.gi_frame)
print(a.gi_frame.f_lasti == b.gi_frame.f_lasti)
print(a.gi_frame.f_locals['x'] == b.gi_frame.f_locals['x'])
print(a.gi_frame.f_locals['x'] is b.gi_frame.f_locals['x'])
print(a.gi_frame.f_lasti)
print(b.gi_frame.f_lasti)
print(a.gi_frame.f_locals['x'])
print(b.gi_frame.f_locals['x'])
print(a.gi_frame.f_code.co_code)
print(b.gi_frame.f_code.co_code)

print('\n')

a = [(x,y) for x in range(
