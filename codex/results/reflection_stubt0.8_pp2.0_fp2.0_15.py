fn = lambda: None
gi = (i for i in ())
fn.__code__ = 1
gi.__code__ = 1

listcompdef_code = listcomp.__code__
forcomp_code = forcomp.__code__
exceptdef_code = exceptdef.__code__
exceptdef_code2 = exceptdef2.__code__
tryfinallydef_code = tryfinallydef.__code__
tryfinallydef_code2 = tryfinallydef2.__code__
tryfinallydef_code3 = tryfinallydef3.__code__
tryfinallydef_code4 = tryfinallydef4.__code__
asyncfor_code = asyncfor.__code__
asyncfor_code2 = asyncfor2.__code__
asyncfor_code3 = asyncfor3.__code__
asyncfor_code4 = asyncfor4.__code__
tryexceptdef_code = tryexceptdef.__code__
tryexceptdef_code2 = tryexceptdef2.__code__
tryexceptdef_code3 = tryexceptdef3.__code__
tryexceptdef_code4 = tryexceptdef4.__code__
tryexceptdef
