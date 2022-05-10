import weakref

def _set_slot(obj, slot_name, value):
    """Set a slot -- sets the slot, and return True if the slot actually
    needed to be set.
    If a superclass already defined the slot, then the subclass does not need
    to set the slot. By returning True/False here, we avoid the subclass
    calling setattr(obj, slot_name, value) and hence running into an
    infinite loop."""
    if slot_name not in getattr(obj, '__slots__', ()):
        # There is a theoretical risk that we get here "too early",
        # if a subclass sets slots in its __init__ before __init__
        # calls parent class __init__.  As long as the subclass
        # sets slots after its parent classes, this will work.
        setattr(obj, slot_name, value)
        return True
    return False


def base_docstring(mro):
    """Given a list of base class '__init__' methods in MRO order, return the
    first '__doc__' string that is not None or the full
