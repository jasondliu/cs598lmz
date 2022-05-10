fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
print(fn())

import builtins
import dis
import types

def test_code(code, expected_varnames):
    globals_ = {'__builtins__': builtins}
    varnames = code.co_varnames
    assert varnames == expected_varnames
    bytecode = dis.Bytecode(code)
    for instr in bytecode:
        if instr.opname == 'LOAD_GLOBAL':
            assert instr.argval in expected_varnames, (instr.argval, expected_varnames)
    exec(code, globals_)
    for varname in varnames:
        assert varname in globals_, varname

def test_code_func(func):
    test_code(func.__code__, func.__code__.co_varnames)

def test_code_class(cls):
    test_code(cls.__init__.__code__, cls.__init__.__code__.co_varnames)

def test_
