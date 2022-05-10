import gc, weakref, sys

# Experimental: TODO: move to larch

import numpy as np

from larch.larchlib import Empty
from larch.symboltable import Group
from larch.larchlib import call_larch_plugin
from larch import Interpreter, use_plugin_path
use_plugin_path('math')
use_plugin_path('io')

def remove_reference(name, weakrefs, symtable=None):
    "remove a reference to a Group or Symbol from a weakref dictionary"
    if name in weakrefs:
        del weakrefs[name]

def getgroup(_larch=None, _symtable=None, name='', create=False, **kws):
    """
    retrieve or create a group by name, creating a weakref if create=True
    
    """
    if _larch is None:
        _larch = Interpreter()
    g = _larch.symtable.get_symbol(name, create=create)
    if g is not None and create and isinstance(g, Group):
