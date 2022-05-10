gi = (i for i in ())
# Test gi.gi_code is empty before calling next
next(gi)
assert gi.gi_code.co_code == b""

# Test gi.gi_frame is returned correctly
def f():
    return gi_frame
g_frame = f.__code__.co_varnames[0]
def g():
    gi = (v for v in ())
    return gi.gi_frame
assert g().f_locals[g_frame].f_code == g.__code__


# Test builtin StopIteration exception handling
class X(object):
    def __iter__(self):
        return self
    def __next__(self):
        raise StopIteration
    def __length_hint__(self):
        return 1

def f():
    try:
        for x in X():
            print(x)
            raise ValueError
    except ValueError:
        pass
    else:
        print('ok')

f()

x = X()
try:
    x.__length_hint__()
except StopIteration:
    print('
