import gc, weakref

#=============================================================================
#
#=============================================================================

class _Base(object):
    """
    Base class for all objects in the API.
    """
    def __init__(self, handle):
        self._handle = handle

    def __del__(self):
        try:
            self._handle.delete()
        except:
            pass

#=============================================================================
#
#=============================================================================

class _BaseWithChildren(_Base):
    """
    Base class for all objects in the API that have children.
    """
    def __init__(self, handle):
        super(_BaseWithChildren, self).__init__(handle)
        self._children = []

    def __del__(self):
        for child in self._children:
            try:
                child._handle.delete()
            except:
                pass
        super(_BaseWithChildren, self).__del__()

#=============================================================================
#
#=============================================================================

