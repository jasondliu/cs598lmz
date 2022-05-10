fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code

# pypy/module/imp/import_all.py:
try:
    raise ImportError
except Exception:
    ei = sys.exc_info()
ei = (ei[0], ei[1], None)

# pypy/module/gc/tracker.py:
def get_rpy_roots():
    """ Get references to objects tracked by the GC, returning them in a
    list.  Note that this includes weakrefs which may have been invalidated
    by a previous collection."""
    roots = []
    roots.append(sys.modules)
    roots.append(sys.getobjects(0))
    roots += sys._current_frames().values()
    gc_module = sys.modules.get('gc', None)
    if gc_module is not None:
        roots.append(gc_module.garbage)
    roots.append(get_rpy_roots) # useless, just for the fun
    return roots
get_rpy_roots()
