fn = lambda: None
gi = (i for i in ())
fn.__code__ = f.__code__
fn.func_code = code = f.func_code
ext = dispatch[code.co_name](fn, code)
closure_iters = []
if ext is not None:
    closure_iters.append(ext.closure_iters)
closure_iters.append(gi)
dct = ext if ext is not None else f
cellvars = dct.__code__.co_cellvars
closure_cells = [CellType(closure_iters[0].next())
                 for name in cellvars]
freevars = dct.__code__.co_freevars
closure_iters.append(gi)
closure_cells += [CellType(closure_iters[-1].next())
                  for name in freevars]
globals = dct.__globals__
global_names = set(dct.__code__.co_names)
global_names &= set(globals)
closure_iters.append(gi)
closure_cells += [CellType(closure_iters[-1].
