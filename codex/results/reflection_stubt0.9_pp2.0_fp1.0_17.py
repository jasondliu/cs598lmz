fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__closure__ = 3
fn.__closure__

print(dir(gi))
print('gi.__name__:', gi.__name__)
print('gi.__code__', gi.__code__)
print('gi.__defaults__', gi.__defaults__)
print('gi.__globals__', gi.__globals__)
print('gi.__dict__', gi.__dict__)
print('gi.gi_frame', gi.gi_frame)
print('gi.gi_running', gi.gi_running)
print('gi.gi_code', gi.gi_code)
print('gi.gi_yieldfrom', gi.gi_yieldfrom)
print('gi.gi_running', gi.gi_running)
print('-'*20)

from types import FunctionType, CodeType

fn = lambda: 1
print(dir(fn))
print(fn.__closure__)
print(fn.__code__)
print(type(fn.__code__),
