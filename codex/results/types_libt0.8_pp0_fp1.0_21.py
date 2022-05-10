import types
types.CodeType(len(co_varnames),
                0, # stack size
                2, # flags
                co_code,
                co_consts,
                co_names,
                co_varnames,
                'gen_fn', # name
                'gen_fn', # filename
                1, # firstlineno
                co_lnotab)

# WTF?
# def gen_fn():
#     a = yield 1
#     b = yield a + 1
#     yield b + 1

print('\nGenerator function...')
gen = gen_fn()
print(gen)
print(next(gen))
print(gen.send(1))
print(gen.send(2))
print(next(gen))
