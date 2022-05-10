import _struct
import _dbus_bindings as dbus_bindings

# The method argument signature is always a tuple.  If we get a list,
# it's a bug.
assert type((dbus_bindings.SIGNATURE_STRING,)) == tuple

def _variant_equal(a, b):
    assert type(a) == type(b)
    if isinstance(a, (int, long, float, basestring, tuple)):
        return a == b
    elif isinstance(a, dbus_bindings.Array):
        return a.value == b.value
    elif isinstance(a, dbus_bindings.Dictionary):
        return a.iteritems() == b.iteritems()
    elif isinstance(a, dbus_bindings.ByteArray):
        return a.value == b.value
    elif isinstance(a, dbus_bindings.Struct):
        return a.value == b.value
    elif isinstance(a, dbus_bindings.ObjectPath):
        return a.value == b.value

