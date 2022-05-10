import weakref
# Test weakref.ref handling of weakrefable objects.
import weakrefable
# Test weakref.ref and weakref.ProxyType handling of non-weakrefable objects.
import nonweakrefable
# Test weakref.ref and weakref.ProxyType and weakref.CallableProxyType handling
# of classes that don't override tp_traverse.
import oldstyle
# Test weakref.ref and weakref.ProxyType handling of old-style classes.
import oldstyle_traverse
# Test weakref.ref and weakref.ProxyType handling of objects with a finalizer.
import finalizable
# Test weakref.ref and weakref.ProxyType handling of objects with
# a non-weakrefable tp_traverse hook.
import oldstyle_nonweakrefable
# Test weakref.ref and weakref.ProxyType handling of objects with a
# weakly-refable tp_traverse hook.
import oldstyle_weakrefable
# Test weakref.ref and weakref.ProxyType handling of objects with a
# non-weakrefable tp_traverse hook and a finalizer.
import finalizable_non
