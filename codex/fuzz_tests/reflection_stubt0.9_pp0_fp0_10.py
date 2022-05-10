fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
if "".__code__.co_lnotab:
    raise RuntimeError("__code__.co_lnotab was not cleared on function creation")

def fn():
    while 1:
        yield 666
gen = fn()
gen.__code__ = gi.gi_code
print(next(gen))
print(next(gen))
print(next(gen))
""")

test_bytecode("__code__.co_lnotab cleared at CPython level")

test_code((asm,), errormsg="")

test_code((asm, asm), errormsg="")

test_bytecode("out-of-bounds lnotab values (CPython-level check)")

test_code((asm, asm, asm), errormsg="")

test_bytecode("out-of-bounds lnotab values (CPython-level check)")

test_code((asm, asm, asm, asm), errormsg="")

##########
# Bytecode swapping
########
