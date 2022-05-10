import types
types.MethodType(m, 'foo')

# function
def f():
    pass

types.FunctionType(f.func_code, f.func_globals, 'foo', f.func_defaults, f.func_closure)

# traceback
def gen_traceback(f):
    try:
        f()
    except:
        return sys.exc_info()[2]

tb = gen_traceback(lambda: 1/0)
# tb.tb_frame, tb.tb_lasti, tb.tb_lineno, tb.tb_next

# frame
f.f_code, f.f_globals, f.f_locals

# slice
s = slice(1, 10, 2)
s, s.start, s.stop, s.step

# buffer
buffer('abc')

# memoryview

# ellipsis

# NotImplementedType
NotImplemented

# xrange
xrange(1, 10, 2)

# complex
3+4
