fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


def f(arg):
    return repr(arg)


s = 'a bc  d  \t \n                                            e'
saf = f(s)
check(saf == "'a bc  d  \\t \\n                                            e'")

try:
    f(0)
except TypeError:
    check(True)
else:
    check(False)

try:
    f(InstanceMethod)
except TypeError:
    check(True)
else:
    check(False)

check(f(666j) == '666j')
check(f(complex(1, 2)) == '(1+2j)')

try:
    f(666l)
except TypeError:
    check(True)
else:
    check(False)

# Gensuit
check(f(gi) == "<generator object <lambda> at 0x%x>" % id(gi))
check(f(gi.gi_frame) == "<frame object at 0x%x>" % id(gi.gi_frame))
check(f(
