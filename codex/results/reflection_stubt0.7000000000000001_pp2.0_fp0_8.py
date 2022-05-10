fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del fn, gi

def _new_code(argcount, posonlyargcount, kwonlyargcount, nlocals, stacksize, flags,
              codestring, consts, names, varnames, filename, name, firstlineno,
              lnotab, freevars, cellvars):
    return types.CodeType(argcount, posonlyargcount, kwonlyargcount, nlocals, stacksize, flags,
                          codestring, consts, names, varnames, filename, name, firstlineno,
                          lnotab, freevars, cellvars)

def _new_code_with_domain_name(argcount, posonlyargcount, kwonlyargcount, nlocals, stacksize, flags,
                               codestring, consts, names, varnames, filename, name, firstlineno,
                               lnotab, freevars, cellvars):
    return types.CodeType(argcount, posonlyargcount, kwonlyargcount, nlocals, stacksize, flags,
                          codest
