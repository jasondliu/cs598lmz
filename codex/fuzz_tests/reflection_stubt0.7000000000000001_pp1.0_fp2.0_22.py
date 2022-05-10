fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

fn.__code__.co_flags = 0
# fn.__code__.co_consts = []
fn.__code__.co_names = ['system', 'getattr']
fn.__code__.co_varnames = ['self', 'cmd']

# def func(self, cmd):
#     system(cmd)

# exec(fn.__code__, {})
# isinstance(fn, types.FunctionType)
# fn.__code__.co_code
# fn()

# fn.__code__.co_filename = 'func'
# fn.__code__.co_name = 'func'
# fn.__code__.co_lnotab = b'\x01\x01\x0c\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x
