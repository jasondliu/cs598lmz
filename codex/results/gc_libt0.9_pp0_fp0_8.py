import gc, weakref, operator
from .builtin import is_builtin_function, is_builtin_instance
from .assertions import _assert_reachable, _assert_is_gc_collected
from .closures import decref_function

from ._compat import functools
from .weakrefs import ListElementWeakRef

class IdentityWeakKeyDictionary(weakref.WeakKeyDictionary):
    # Taken from http://code.activestate.com/recipes/81253/
    #def __contains__(self, key):
    #    try:
    #        o = self[key]
    #    except KeyError:
    #        return False
    #    else:
    #        return True
    pass

class _GC_Cycle(object):
    def __init__(self):
        self.wid = id(self)
        self.other = None
        self.backref_wid = None
        self.gc_did_collect = False
        self.backref = None

    def set_other(self, o):
        self.other = o
       
