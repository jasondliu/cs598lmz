from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print('a: {}'.format(a))
print('b: {}'.format(b))
print('a is b: {}'.format(a is b))
print('a == b: {}'.format(a == b))
print('a is iter(b): {}'.format(a is iter(b)))
print('')

print('a.gi_code: {}'.format(a.gi_code))
print('a.gi_code is b.gi_code: {}'.format(a.gi_code is b.gi_code))
print('a.gi_frame: {}'.format(a.gi_frame))
print('a.gi_frame is b.gi_frame: {}'.format(a.gi_frame is b.gi_frame))
print('')

print('type(a): {}'.format(type(a)))
print('type(a.gi_code): {}'.format(type(a.gi_code)))
print('type(a.gi_frame): {}'.format(type(a.gi_frame)))
