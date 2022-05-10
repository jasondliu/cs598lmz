from types import FunctionType
list(FunctionType('f', globals(), 'return a+a'))

list(FunctionType('f', globals(), 'return a+a', ('a',), ('a')))

list(FunctionType('f', globals(), 'return a+a', ('a',), () , 1))

FunctionType('f', globals(), 'return a+a', ('a',), (), 1, '<>', '<>', 2, (1,))

def f(x): return x

f.func_name

f.func_doc

f.func_defaults

f.func_globals is globals()

f.func_code

f.func_closure

f.func_dict

f.func_code.co_code == bytes(
    (124, 0, 0, 0, 100, 0, 1, 0, 100, 0, 0, 0, 83, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0,
