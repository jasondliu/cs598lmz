import gc, weakref, time, sys

_weakref_type = type(weakref.ref(1))

def _format_object(o):
    try:
        return o.__class__.__name__ + " object"
    except AttributeError:
        return type(o)

def _format_object_key(o):
    try:
        return o.__class__.__name__
    except AttributeError:
        return type(o)

def _format_object_value(o):
    try:
        return repr(o)
    except AttributeError:
        return type(o)

def _name_of(o):
    try:
        return o.__name__
    except AttributeError:
        return str(o)

def _qstr(s):
    return '"%s"' % (s,)

def _format_ref_chain(chain):
    lines = []
    for i, (ref, depth) in enumerate(chain):
        if depth == 0:
            lines.append("%d: %s" % (
