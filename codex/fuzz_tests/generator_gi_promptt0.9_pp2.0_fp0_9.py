gi = (i for i in ())
# Test gi.gi_code is None when created from iter(gi)
iter_gi = iter(gi)
print
print 'gi.gi_frame.f_code == <code object func at ', gi.gi_frame.f_code, '>'

def func(n):
    return n * 2

print 'func.func_code == <code object func at ', func.func_code, '>'

gi2 = (n for n in ())
gi2.gi_code = func.func_code
print 'next(iter(gi2)) =>', next(iter(gi2))
