import _struct
import _io
import _codecs
import _random
import _operator
import _collections
import _heapq
import _symtable
import _weakref
import _pickle
import _json
import _sre
import itertools
import builtins

_all = [_imp, _io, _codecs, _random, _operator, _collections, _heapq, _symtable,
        _weakref, _pickle, _json, _struct, _sre]
if sys.version_info[:2] >= (2, 7):
    _all.append(itertools)
if sys.version_info[:2] > (3, 2):
    _all.append(builtins)

def add_builtins(space):
    for mod in _all:
        mod.setup(space)
    space.text_w = space.wrap('')
    space.int_w = space.wrap(0)
    space.uint_w = space.wrap(0)

