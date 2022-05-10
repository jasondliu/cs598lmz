fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.func_code = gi.gi_code = type(
    'code', (object,), dict(co_name='<lambda>'))()

# A global dict mapping object ids to a list of weak
# references to the object. This is for use by assert_*_equal
# functions in TestCase classes.
_imn_objects = {}

def _list_object(obj):
    """Add list of weak references to obj to _imn_objects[id(obj)].
    """
    oid = id(obj)
    olist = _imn_objects.get(oid)
    if olist is None:
        olist = _imn_objects[oid] = []
    olist.append(weakref.ref(obj))

def _remove_object(obj):
    """Remove all weak references to obj from _imn_objects[id(obj)].
    """
    oid = id(obj)
    olist = _imn_objects.get(oid)
    if olist is not None:
        for i,oref in enumerate
