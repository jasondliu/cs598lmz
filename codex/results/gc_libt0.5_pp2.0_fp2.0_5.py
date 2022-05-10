import gc, weakref

#------------------------------------------------------------------------------

def _get_trash_can():
    """Return the trash can singleton."""
    try:
        return _trash_can
    except NameError:
        global _trash_can
        _trash_can = TrashCan()
        return _trash_can

#------------------------------------------------------------------------------

def trash(obj, *args):
    """Put an object into the trash can.

    The object will be deleted when no reference to it exists.
    """
    _get_trash_can().add(obj, *args)

#------------------------------------------------------------------------------

def untrash(obj):
    """Remove an object from the trash can.

    The object will no longer be deleted.
    """
    _get_trash_can().remove(obj)

#------------------------------------------------------------------------------

def clear_trash():
    """Delete all objects from the trash can.

    This will also delete all objects referenced by the objects in the trash can.
    """
    _get_trash_can().clear()

#------------------------------------------------------------------------------

class TrashCan(object):
   
