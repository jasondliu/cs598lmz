fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_flags = 127
fn.__code__.co_consts = (1, )
fn_c = code.FunctionCode(fn, code.symbol_table)

# 0x0 == CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE
fn_c.co_flags = 0
fn_c.co_consts = (1, 2, 3, None)
fn2 = fn_c.to_pyfunc()

def fn3():
    print(1)
fn_c = code.FunctionCode(fn3, code.symbol_table)
fn_c.co_flags = 0
fn_c.co_consts = (1, 2, 3, None)
fn4 = fn_c.to_pyfunc()

print(fn3.__code__)
print(fn4.__code__)
