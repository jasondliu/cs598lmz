gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
gi_code = gi.gi_code
gi_frame = gi.gi_frame

# CPython 3.2 code object and not
# http://bugs.python.org/issue12207
co = type(gi_code)()
co_code = co.co_code
not_co = type(co)()

# CPython 3.2 frame object
f = type(gi_frame)()

# CPython 3.2 function object
def f():
    pass
f = type(f)()


class SubType(int):
    pass


class Type(object):
    def f(self):
        pass

    def g(self):
        yield 1

    def __repr__(self):
        return 'Type()'

Type_f = Type.f
Type_g = Type.g

t = Type()
assert repr(t) == 'Type()'
t = Symbol('t', SubType)
assert t._type is SubType
assert t.value == SubType
s = Symbol('s', t)

