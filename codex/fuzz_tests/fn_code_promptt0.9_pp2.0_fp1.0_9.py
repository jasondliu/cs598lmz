fn = lambda: None
# Test fn.__code__.__hash__().
old_id = id(fn.__code__)
fn()
hash(fn.__code__)
new_id = id(fn.__code__)
assert new_id != old_id

# Test all the attributes of a __code__ object that the interpreter uses
# for a no-arg, no-return function.
def named(abc, xyz):
    return

c = named.__code__
c.co_argcount
c.co_kwonlyargcount
c.co_nlocals
c.co_stacksize
c.co_code
c.co_consts
c.co_names
c.co_varnames
c.co_filename
c.co_name
c.co_firstlineno

# Check that code.co_consts contains the right number of consts
def func(unused_arg, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t,
         u, v,
