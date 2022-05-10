fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #5: cannot use keyword 'in'

def f(**kwargs):
    if 'in' in kwargs:
        return kwargs['in']
    return 'out'

assert f(in=2) == 2
assert f(out=2) == 'out'
assert f(**{'in': 2}) == 2
assert f(**{'out': 2}) == 'out'

# Issue #6: cannot assign to 'f'

f = 2

# Issue #7: cannot assign to 'f'

f = (lambda f: f)

# Issue #8: cannot assign to '__all__'

__all__ = 2

# Issue #9: cannot assign to 'f'

f = (lambda f: (lambda: f))

# Issue #10: cannot assign to 'f'

f = (lambda f: (lambda f: f))

# Issue #11: cannot assign to 'f'

f = (lambda f: (lambda f: (lambda f: f)))

# Issue
