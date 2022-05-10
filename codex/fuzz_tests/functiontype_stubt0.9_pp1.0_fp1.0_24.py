from types import FunctionType
a = (x for x in [1])
a.gi_frame.f_code
a.gi_frame.f_code.__class__
a.gi_frame.f_code.co_name
a.gi_frame.f_code.co_varnames
a.gi_frame.f_code.co_argcount
a.gi_frame.f_code.__name__
a.gi_frame.f_code.co_filename
a.gi_frame.f_code.co_firstlineno
def new_func():
    a = 100
new_func = FunctionType(a.gi_frame.f_code, globals(), "new_func")
new_func()
def f_func():
    b = 100
f_func.__code__ = a.gi_frame.f_code
f_func()
 
 
a = (x for x in [1,2,3])
next(a)
# a.gi_frame.f_code.co_name
# a.gi_frame.f_code.co_varnames
# a.gi_frame.f_
