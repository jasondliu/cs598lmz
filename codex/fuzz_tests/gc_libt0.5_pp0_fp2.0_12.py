import gc, weakref
from gc import get_objects, get_referrers
from weakref import ref
from pypy.interpreter.error import OperationError, oefmt
from pypy.interpreter.gateway import unwrap_spec
from rpython.rlib import rgc
from rpython.rlib.objectmodel import keepalive_until_here, we_are_translated


@unwrap_spec(w_obj=W_Root)
def print_refs(space, w_obj):
    """Print a list of all objects reachable from w_obj."""
    w_obj = _get_weakrefable(space, w_obj)
    w_dict = space.newdict()
    w_dict.initialize_content([])
    w_dict.setitem(space, w_obj, space.w_None)
    print_refs_inner(space, w_dict, w_obj, 0)

def print_refs_inner(space, w_dict, w_obj, depth):
    w_type = space.type(w_obj
