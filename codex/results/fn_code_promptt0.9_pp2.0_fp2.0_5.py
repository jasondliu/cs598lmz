fn = lambda: None
# Test fn.__code__.co_varnames:
meta.__code__.co_varnames
meta.__code__.co_argcount
 
lmbd.__code__.co_argcount
lmbd.__code__.co_varnames    # ? Why 1?

# Import function:
from 
 
# Load function from meta:
meta_fn = globals()[meta.__code__.co_varnames[0]]
meta_fn()
 
# Write another meta, get another func:
import importlib
import meta
meta_fn = importlib.import_module('meta').__code__.co_varnames[0]
globals()[meta_fn] = eval(f'globals()["{meta_fn}"]')
globals()[meta_fn]() 
 
# Once and for all:
import importlib
meta_fn = importlib.import_module('meta').__code__.co_varnames[0]
eval('.'.join(['globals()', '"' + meta_fn + '
