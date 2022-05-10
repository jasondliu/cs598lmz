import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_uint, ctypes.c_double, ctypes.c_void_p)

capi = {}


def catdms(nterms, x, funs):
    dms = 0.0
    for i in range(nterms):
        dms += funs[i](x)
    return dms

capi['catdms'] = FUNTYPE(catdms)


def catdms_n():
    return len(catdms_functions())

capi['catdms_n'] = len(catdms_functions())


def catdms_functions():
    import inspect
    frame = inspect.currentframe()
    return [getattr(frame.f_back.f_locals[k], '__name__')
      for k in list(frame.f_back.f_locals.keys())
      if callable(frame.f_back.f_locals[k]) and k[0]!='_']

capi['catdms_functions'] = cat
