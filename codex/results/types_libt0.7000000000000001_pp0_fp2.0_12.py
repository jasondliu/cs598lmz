import types
types.__all__ += ["LazyObject"]

# Monkeypatch the reload() function
#
# This is done because we want to modify the behaviour of module reloading in a
# way that is not possible using the existing API.

# First, we save the original reload() function
old_reload = reload

# Next, we create a wrapper function around the original reload() function
def lazy_reload(module):
    """
    The wrapper function that is monkey-patched into place.
    """
    if isinstance(module, LazyObject):
        # If the given module is a lazy object, we want to reload the module
        # this object is proxying.
        module = module._wrapped
    return old_reload(module)

# Finally, we monkey-patch the reload() function with our wrapper
reload = lazy_reload
