fn = lambda: None
gi = (i for i in ())
fn.__code__ = (1, 0, 1, 67, b'string', (), (), ('x', 'y'), '', '', 1, b'string\x00\x00\x00', (), (), ())
fn.__code__.co_consts = (None, None)
fn.__closure__ = (gi,)
dis(fn)
# "disasm" does not work for generator functions, see issue23209:
# dis(fn)
print()

# Bytecode containing name with empty string, and a lambda
dis(compile("""lambda x, **y: x + y[""]""", "<string>", "eval"))
# Bytecode containing function call with no positional arguments:
# dis(compile("""def f(): return (x for x in ())""", "<string>", "exec"))
print()

# Bytecode retrieved from function using different encoding
def fn():
    pass
compiled = compile(fn.__code__, fn.__code__.co_filename, "exec")
dis(compiled)
print()

# Bytecode retrieved from function in a different module
class A:
