import types
# Test types.FunctionType
def f():
    pass
f.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
f.__code__.co_filename = 'x'
f.__closure__ = (None, )
f.__defaults__ = None
f.__globals__ = globals()
f.__dict__ = {'a': 1}
print(f.func_code.co_filename)
print(f.func_closure)
print(f.func_defaults)
print(f.func_globals is globals())
print(f.func_dict['a'])

# Test types.MethodType
class C(object):
    def f(self):
        pass
C.f.__code__ = types.CodeType(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
C.f.__code__.co_filename = 'x'
C.f.__closure__ = (None, )
C.f.__
