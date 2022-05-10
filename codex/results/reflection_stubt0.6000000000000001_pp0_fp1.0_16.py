fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
'''
import dis
dis.dis(fn)

# fn.__code__.co_code
# fn.__code__.co_consts
# fn.__code__.co_firstlineno
# fn.__code__.co_flags
# fn.__code__.co_lnotab
# fn.__code__.co_name
# fn.__code__.co_names
# fn.__code__.co_nlocals
# fn.__code__.co_stacksize
# fn.__code__.co_varnames

# fn.__code__.co_consts[0]
# fn.__code__.co_consts[0].__code__
# fn.__code__.co_consts[0].__code__.co_code
# fn.__code__.co_consts[0].__code__.co_consts
# fn.__code__.co_consts[0].__code__.co_firstlineno
# fn.__code__.co_consts
