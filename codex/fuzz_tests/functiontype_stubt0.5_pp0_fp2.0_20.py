from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))

print(a.gi_frame)
print(a.gi_frame.f_code)
print(a.gi_frame.f_code.co_name)
print(a.gi_code)
print(a.gi_code.co_name)
print(a.gi_frame.f_locals)
print(a.gi_frame.f_locals.get('x'))
print(a.gi_frame.f_locals.get('x'))
print(a.gi_frame.f_locals.get('x'))
print(a.gi_frame.f_locals.get('x'))
print(a.gi_frame.f_locals.get('x'))
print(a.gi_frame.f_locals.get('x'))
print(a.gi_frame.f_locals.get('x'))
