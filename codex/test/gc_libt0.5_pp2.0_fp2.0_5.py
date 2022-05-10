import gc, weakref

#------------------------------------------------------------------------------

def _get_trash_can():
    """Return the trash can singleton."""
