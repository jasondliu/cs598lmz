fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.func_code = types.CodeType(
    0, 0, 0, 0, b"c", (), (), (), "", "", 0, b"", ())
fn.func_globals.update({
    "LambdaType": LambdaType,
    "fn": fn,
    "gi": gi
})
bytecode.opmap['LOAD_GENEXPR'] = bytecode.opmap['LOAD_CLOSURE'] + 1


def genwrap(code, *consts):
    return types.CodeType(code.co_argcount,
                          code.co_nlocals,
                          code.co_stacksize,
                          code.co_flags,
                          code.co_code,
                          consts,
                          code.co_names,
                          code.co_varnames,
                          code.co_filename,
                          code.co_name,
                          code.co_firstlineno,
                          code.co_lnotab,
                          code.co_freevars,
                          code.co
