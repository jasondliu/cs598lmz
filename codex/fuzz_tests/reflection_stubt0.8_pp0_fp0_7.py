fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()
```

```
codetype(co_argcount, co_kwonlyargcount, co_nlocals, co_stacksize, co_flags,
         co_code, co_consts, co_names, co_varnames, co_filename, co_name, co_firstlineno,
         co_lnotab, co_freevars, co_cellvars)

type(code, argcount, kwonlyargcount, nlocals, stacksize, flags, codestring,
     constants, names, varnames, filename, name, firstlineno, lnotab[, freevars[, cellvars]])
```

## More references
- [An In-Depth Look at Python Bytecode](https://jeffknupp.com/blog/2014/07/18/improve-your-python-understanding-pythons-execution-model/)
- [关于Python中Bytecode的一些思考](https://www.jiqizhixin.com/articles/
