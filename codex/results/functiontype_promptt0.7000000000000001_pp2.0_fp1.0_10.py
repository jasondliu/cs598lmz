import types
# Test types.FunctionType(types.CodeType(argcount, nlocals, stacksize, flags,
#                                 code, constants, names, varnames, filename,
#                                 name, firstlineno, lnotab[, freevars[, cellvars]]),
#                         globals[, name[, argdefs[, closure]]])
func = types.FunctionType(types.CodeType(0, 0, 0, 0, "", (), (), (), "",
                                         "", 1, ""),
                         {}, "", None, None)
func()

# Test that the repr of a function with a __qualname__ is correct
def foo():
    def bar():
        pass
    bar.__qualname__ = "BAR"
    return bar

baz = foo()
assert repr(baz) == "<function BAR at 0x000001F17FA2D7B8>"

# Test that the repr of a function with a __qualname__ is correct
def foo():
    def bar():
        pass
    bar.__qualname__ = "BAR"
    return bar

b
