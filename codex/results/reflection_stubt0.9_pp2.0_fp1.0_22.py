fn = lambda: None
gi = (i for i in ())
fn.__code__ = 1
fn.__closure__ = gi
stack = inspect.stack()
_getframe_func(stack)
fn.__code__ = 1
try:
    fn()
except ZeroDivisionError:
    pass
print('no error')
f.__code__=''
frame = stack[1][0]
print(frame.f_code)
print(frame.f_code.000)
_getframe_func(stack)
stack = inspect.stack()
_getframe_func(stack)
for i in stack:
    print(i)
    for j in i:
        print(j)
frame = stack
for i in frame:
    print(i)
f.__code__=''
inspect.isframe
tst = r'''{'args': 'hits_self', 'file': 'KotOR 1 - Item descriptions.py', 'frame': <frame object>, 'function': 'get_frame_func_name', 'lineno': 16, 'module': 'KotOR 1 - Item descriptions', 'code_context': ['return string if string != "" else
