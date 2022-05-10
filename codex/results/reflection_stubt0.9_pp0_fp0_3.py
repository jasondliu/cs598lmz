fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code  # TODO: remove
setattr(fn, 'gi_code', gi.gi_code)  # TODO: remove
fn.__name__ = '<lambda>'
del gi  # TODO: remove
fi = fn()
# TODO: this is missing
# fi.__name__ = '<lambda>'; fi
# TODO: why does this fail? there is nothing in CellType.ob_ref that is not accessible via __pep__



## http://pypi.python.org/pypi/typed_ast/
##     > Typed AST is an experimental branch that implements a full type-inference Python interpreter
##     > with a Prolog backend, which I think would be good to build a community around and possibly
##     > merge into the main branch at some point.
# import typed_ast as t
# import ast as t
# import dis; dis.dis(t.parse('1 + 1', mode='eval'))



## Meta classes are just classes that return an object that supports a few different protocols...
## https://spe
